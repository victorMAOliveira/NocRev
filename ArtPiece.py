from abc import ABC, abstractmethod
from enum import Enum, auto


class Gender(Enum):
    HORROR = auto()
    ACTION = auto()


class Type(Enum):
    MOVIE = auto()
    SERIES = auto()
    EPISODE = auto()


class Status(Enum):
    UNSEEN = auto()
    WATCHING = auto()
    COMPLETED = auto()


class ArtPiece(ABC):
    def __init__(self, name: str, gender: Gender, type: Type, status: Status):
        self.name = name
        self.gender = gender
        self.type = type
        self.status = status


class Movie(ArtPiece):
    def __init__(self, name: str, gender: Gender, type: Type):
        super().__init__(name, gender, type)


class Series(ArtPiece):
    def __init__(self, name: str, gender: Gender, type: Type, episodes: list[Episode]):
        super().__init__(name, gender, type)
        self.episodes = episodes


class Episode(ArtPiece):
    def __init__(self, name: str, gender: Gender, type: Type, fatherSeries: Series):
        super().__init__(name, gender, type)
        self.fatherSeries = fatherSeries
