import enum
from typing import Generic, List, TypeVar
from pydantic import BaseModel, ConfigDict, Field, conint

class ListRequest(BaseModel):
    page: int = Field(1, ge=1)
    per_page: int = Field(50, ge=1, le=500)

T = TypeVar("T")

class PagedResponse(BaseModel, Generic[T]):
    current_page: int
    last_page: int
    total: int
    data: List[T]
    
    model_config = ConfigDict(
         from_attributes = True
     )