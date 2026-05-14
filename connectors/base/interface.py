from abc import ABC, abstractmethod


class BaseConnector(ABC):
    name: str

    @abstractmethod
    def test_connection(self) -> dict:
        raise NotImplementedError

    @abstractmethod
    def execute_action(self, action: str, payload: dict) -> dict:
        raise NotImplementedError
