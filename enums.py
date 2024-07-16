from enum import IntEnum, auto


class SMBOX_ICON_TYPE(IntEnum):
    ICON_NONE = auto(),
    ICON_WARNING = auto(),
    ICON_ERROR = auto(),
    ICON_INFO = auto()


class OPEN_WINDOW_TYPE(IntEnum):
    WINDOW_MAIN = 1,
    WINDOW_CONFIG = 2,
    WINDOW_SHOWS = 3,
