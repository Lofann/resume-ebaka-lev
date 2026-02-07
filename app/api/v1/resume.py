from fastapi import APIRouter, Depends, HTTPException, Path, UploadFile, status, Query, Body
import logging


logger = logging.getLogger(__name__)

resume_router = APIRouter()

