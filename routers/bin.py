from fastapi import APIRouter, HTTPException, Request
from models.schemas import BinCreate, BinView
from core.database import prisma
from utils.slug import gen_slug
from utils.expiry import calc_expiry
from datetime import datetime, timezone

router = APIRouter(prefix="/bin", tags=["bin"])

@router.post("", response_model=BinView)
async def create_bin(request: Request, data: BinCreate):
    slug = data.slug or gen_slug()

    expires_at = calc_expiry(data.expiry_choice)

    try:
        new_bin = await prisma.bincontents.create(
            data={
                "slug": slug,
                "title": data.title,
                "content": data.content,
                "language": data.language,
                "wrap_text": data.wrap_text,
                "burn_after_read": data.burn_after_read,
                "expires_at": expires_at,
                "user_meta": {
                    "create": {
                        "ip_address": request.client.host,
                        "user_agent": request.headers.get("user-agent", "unknown"),
                    }
                },
            },
            include={"user_meta": True}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return BinView(
        slug=new_bin.slug,
        title=new_bin.title,
        content=new_bin.content,
        language=new_bin.language,
        wrap_text=new_bin.wrap_text,
        burn_after_read=new_bin.burn_after_read,
        expires_at=new_bin.expires_at,
        created_at=new_bin.created_at
    )

@router.get("/{slug}", response_model=BinView)
async def read_bin(slug: str):
    bin = await prisma.bincontents.find_unique(
        where={"slug": slug}
    )

    if not bin:
        raise HTTPException(status_code=404, detail="Bin not found")

    if bin.expires_at and bin.expires_at < datetime.now(timezone.utc):
        raise HTTPException(status_code=410, detail="Bin expired")

    if bin.burn_after_read:
        await prisma.bincontents.delete(where={"slug": slug})

    return BinView(
        slug=bin.slug,
        title=bin.title,
        content=bin.content,
        language=bin.language,
        wrap_text=bin.wrap_text,
        burn_after_read=bin.burn_after_read,
        expires_at=bin.expires_at,
        created_at=bin.created_at
    )
