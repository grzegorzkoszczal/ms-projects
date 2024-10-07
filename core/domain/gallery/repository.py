from abc import ABC, abstractmethod
from typing import Any, List, Optional

from core.domain.models import SortOrderEnum
from core.domain.gallery.models import Gallery, GallerySortByEnum


class GalleryRepositoryPort(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def create(self, item: Gallery) -> Gallery:
        pass