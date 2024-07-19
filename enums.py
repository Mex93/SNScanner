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


class SN_COUNT_TYPE(IntEnum):
    SN_DOUBLE = 1,
    SN_TRIPLE = 2,
    SN_NONE = 3,

class PROJECT_TYPE(IntEnum):
    NEW_PROJECT = 1,
    OPENNED_PROJECT = 2,
    NONE_PROJECT = 3,

class PROGRAM_STATUS(IntEnum):
    NO_PROJECT = 1,
    IN_JOB = 2,

class FIELD_INDEX_ARR_TYPE(IntEnum):
    SN_1 = 0,
    SN_2 = 1,
    SN_3 = 2,
    SCAN_DATA = 3,
    RESULT_STATUS = 4,
    SQL_INDEX = 5

class FIELD_TYPE_ID(IntEnum):
    NUMBER_LABEL = 0,
    SN_1 = 1,
    SN_2 = 2,
    SN_3 = 3,
    HORIZONTAL_SPACER = 4,
    SCAN_DATA = 5,
    RESULT_STATUS = 6,

class CONFIG_MENU_FIELD_TYPE(IntEnum):
    SN_ONE = 1,
    SN_TWO = 2,
    SN_TRI = 3,
    PROJECT_NAME = 4,
    LOT_COUNT = 5,
    SNS_COUNT = 6,
    MAX_LOT_COUNT = 7

class FIELD_TYPE(IntEnum):
    TEXT_LABEL = 1,
    INPUT_AREA = 2,
    SPACER = 3,

class WINDOW_TYPE(IntEnum):
    CREATE = 1,
    CONFIG = 2,
    OPEN = 3,

