from enum import Enum


class TTL(str, Enum):
    FIVE_MIN = '5min'
    THIRTY_MIN = '30min'
    ONE_HOUR = '1hour'
    FOUR_HOURS = '4hours'
    TWELVE_HOURS = '12hours'
    ONE_DAY = '1day'
    ONE_WEEK = '1week'
