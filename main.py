
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.database import init_db, close_db
from routers.bin import router as bin_router
from routers.metadata import router as metadata_router

app = FastAPI(title="Bins API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js origin
    allow_credentials=True,                    
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.on_event("shutdown")
async def on_shutdown():
    await close_db()

app.include_router(bin_router)
app.include_router(metadata_router)
