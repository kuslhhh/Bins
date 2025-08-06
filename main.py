from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from core.database import init_db, close_db
from routers.bin import router as bin_router
from routers.metadata import router as metadata_router

app = FastAPI(title="Bins API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins in development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.on_event("startup")
async def on_startup():
    try:
        await init_db()
    except Exception as e:
        print(f"Database connection failed: {e}")
        raise HTTPException(status_code=500, detail="Database connection failed")

@app.on_event("shutdown")
async def on_shutdown():
    await close_db()

app.include_router(bin_router)
app.include_router(metadata_router)
app.include_router(metadata_router)
