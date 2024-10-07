from core.domain.models import SortOrderEnum
from core.domain.gallery.models import Gallery, GalleryStatus, GallerySortByEnum
from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import datetime 
from typing import Dict, List, Optional
from entrypoints.api.v1.schemas.common import ListRequest


class GalleryBase(BaseModel):
    project_code: str
    project_name: str


class UsersListRequest(ListRequest):
    sort_by: Optional[GallerySortByEnum] = GallerySortByEnum.id
    sort_order: Optional[SortOrderEnum] = SortOrderEnum.asc
    status: Optional[GalleryStatus] = None
    search: Optional[str] = None