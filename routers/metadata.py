from fastapi import APIRouter, HTTPException
from core.database import prisma
from models.schemas import UserMetaView

router = APIRouter(prefix="/metadata", tags=["metadata"])

@router.get("/{slug}", response_model=list[UserMetaView])
async def get_user_metadata(slug: str):
    metas = await prisma.UserMetadata.find_many(where = {"bin_slug": slug})
    if not metas:
        raise HTTPException(status_code=404, detail="No metadta found for this bin")
    return [UserMetaView(**m.dict()) for m in metas]