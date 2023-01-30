import datetime
from typing import (
    Optional
)

from nonebot.adapters.onebot.v11 import Message


class RawNews:
    message: Message
    __start_time: float
    __end_time: float

    def __init__(self, message: Message, start_time: Optional[float], end_time: Optional[float]):
        """
        start_time: 起始时间
        end_time: 终止时间
        默认起始时间为现在
        默认终止时间为七天后
        """
        super(RawNews, self).__init__()
        self.message = message
        if start_time is None:
            self.__start_time = datetime.datetime.now().timestamp()
        else:
            self.__start_time = start_time
        if end_time is None:
            self.__end_time = (datetime.datetime.fromtimestamp(self.__start_time) + datetime.timedelta(days=7))\
                .timestamp()
        else:
            self.__end_time = datetime.datetime.fromtimestamp(end_time)

    @classmethod
    def get_raw_news_delta_time_from_str(cls, message: Message, end_time_delta: datetime.timedelta):
        """通过时间差设置终止时间以获得RawNews"""
        return cls(message, datetime.datetime.now().timestamp(), (datetime.datetime.now()+end_time_delta))



