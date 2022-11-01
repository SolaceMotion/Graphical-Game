from enum import Enum, auto


class State(Enum):
    ON_MAP = auto()
    IN_COMBAT = auto()
    IN_MENU = auto()