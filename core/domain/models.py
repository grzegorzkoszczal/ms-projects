from typing import Generic, List, TypeVar
import enum

class SortOrderEnum(enum.Enum):
    asc = "asc"
    desc = "desc"

T = TypeVar("T")

class PagedResult(Generic[T]):
    current_page: int
    last_page: int
    total: int
    data: List[T]

    def __init__(self, current_page: int, last_page: int, total: int, data: List[T]):
        self.current_page = current_page
        self.last_page = last_page
        self.total = total
        self.data = data

    def dump(self) -> dict:
        return {
            'current_page': self.current_page,
            'last_page': self.last_page,
            'total': self.total
        }   
