

from abc import abstractmethod, ABC


class Battery(ABC):

    @abstractmethod
    def needs_service(self) -> bool:
        pass





