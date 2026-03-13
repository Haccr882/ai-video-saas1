from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import auth, video, ai, upload, scheduler, analytics, oauth, payment
from app.core.database import Base, engine
from app.core.logger import logger

app = FastAPI(title="AI Video SaaS API")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(video.router)
app.include_router(ai.router)
app.include_router(upload.router)
app.include_router(scheduler.router)
app.include_router(analytics.router)
app.include_router(oauth.router)
app.include_router(payment.router)

@app.get("/")
def root():
    logger.info("API running")
    return {"status": "AI Video SaaS running"}
