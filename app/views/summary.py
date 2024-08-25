import logging

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi.responses import HTMLResponse
from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import templates
from app.dependencies.db import get_db
from app.models.summary import YoutubeSummary

logger = logging.getLogger(__name__)

PAGINATE_BY_DEFAULT = 10
router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def index(
    request: Request,
    db: AsyncSession = Depends(get_db),
    page: int = 1,
    paginate_by: int = PAGINATE_BY_DEFAULT,
):
    offset = (page - 1) * paginate_by
    limit = paginate_by

    query = select(YoutubeSummary).order_by(func.random()).offset(offset).limit(limit)
    results = await db.execute(query)
    summaries = results.scalars().all()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "summaries": summaries,
            "page": page,
            "paginate_by": paginate_by,
        },
    )


@router.get("/search", response_class=HTMLResponse)
async def search(
    request: Request,
    db: AsyncSession = Depends(get_db),
    query: str = "",
    page: int = 1,
    paginate_by: int = PAGINATE_BY_DEFAULT,
):
    # offset = (page - 1) * paginate_by
    # limit = paginate_by

    query = select(YoutubeSummary).where(
        func.lower(YoutubeSummary.title).contains(query.lower())
    )
    results = await db.execute(query)
    summaries = results.scalars().all()

    return templates.TemplateResponse(
        "search.html",
        {
            "request": request,
            "summaries": summaries,
            "page": page,
            "paginate_by": paginate_by,
            "query": query,
        },
    )


@router.get("/summary/{video_id}", response_class=HTMLResponse)
async def summary(
    request: Request, db: AsyncSession = Depends(get_db), video_id: str = ""
):
    query = select(YoutubeSummary).where(YoutubeSummary.video_id == video_id)
    result = await db.execute(query)
    summary = result.scalars().first()

    return templates.TemplateResponse(
        "summary.html",
        {
            "request": request,
            "summary": summary,
        },
    )


@router.get("/random", response_class=HTMLResponse)
async def random(request: Request, db: AsyncSession = Depends(get_db)):
    query = select(YoutubeSummary).order_by(func.random()).limit(1)
    result = await db.execute(query)
    summary = result.scalars().first()

    return templates.TemplateResponse(
        "summary.html",
        {
            "request": request,
            "summary": summary,
        },
    )


@router.get("/popular", response_class=HTMLResponse)
async def popular(request: Request, db: AsyncSession = Depends(get_db)):
    query = select(YoutubeSummary).order_by(YoutubeSummary.id.desc()).limit(10)
    results = await db.execute(query)
    summaries = results.scalars().all()

    return templates.TemplateResponse(
        "popular.html",
        {
            "request": request,
            "summaries": summaries,
        },
    )