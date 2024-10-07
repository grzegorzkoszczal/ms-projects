from core.domain.common.use_case import UseCaseInterface
from core.domain.gallery.repository import GalleryRepositoryPort

class CreateItemUseCase(UseCaseInterface):
    def __init__(self,
                 item_repository: GalleryRepositoryPort
                 
                 
                ):
        pass