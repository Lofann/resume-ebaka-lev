from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 

from app.api.v1.resume import resume_router

import uuid
import logging
import uvicorn 


# from app.schemas import ResumeRequest
# from app.services.resume_service import create_resume
# from app.services.pdf_service import generate_pdf



logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Resume AI")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8110,
        reload=True,
        log_level="debug"
    )