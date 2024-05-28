from abc import ABC, abstractmethod
from typing import Any

class AbstractCatArray(ABC):
    @abstractmethod
    def __init__(self, initial_data: list = None) -> None:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __getitem__(self, index: int) -> Any:
        pass

    @abstractmethod
    def __setitem__(self, index: int, value: Any) -> None:
        pass

    @abstractmethod
    def append(self, value: Any) -> None:
        pass

    @abstractmethod
    def insert(self, index: int, value: Any) -> None:
        pass

    @abstractmethod
    def index(self, value: Any, start: int = 0, stop: int = None) -> int:
        pass

    @abstractmethod
    def remove(self, value: Any) -> None:
        pass
