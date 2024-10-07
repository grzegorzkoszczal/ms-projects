from typing import Optional


class DomainException(Exception):
    def __init__(self, message: Optional[str], status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)