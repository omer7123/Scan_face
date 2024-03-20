from fastapi import APIRouter
from api.scan import router as scan_router

router = APIRouter()
router.include_router(scan_router)
