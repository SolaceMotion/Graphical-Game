from enum import Enum, auto


class State(Enum):
    ON_MAP = auto()
    IN_COMBAT = auto()
    GAME_OVER = auto()