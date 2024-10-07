from typing import Dict, List
from sqlalchemy import Integer, String, Enum, DateTime, Float
from sqlalchemy.sql import func
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import mapped_column, Mapped
from infrastructure.database import Base
from sqlalchemy.orm import relationship 
import enum


class GallerySortByEnum(enum.Enum):
    id = 'id'
    project_code = 'project_code'
    project_name = 'project_name'
    status = 'status'
    price = 'price'
    created_at = 'created_at'


class GalleryStatus(enum.Enum):
    available = 'available'
    last_items = 'last_items'
    out_of_stock = 'out_of_stock'
    discontinued = 'discontinued'


class Gallery(Base):
    __tablename__ = 'gallery'

    id = Mapped[int] = mapped_column(Integer, primary_key=True, index=True, init=False)
    project_code: Mapped[str] = mapped_column(String, unique=True, index=True)
    project_name: Mapped[str] = mapped_column(String, unique=True, index=True)
    status: Mapped[GalleryStatus] = mapped_column(Enum(GalleryStatus), default=GalleryStatus.available)
    price = Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=False), default=func.now())

    def is_available(self) -> enum:
        return self.sta
