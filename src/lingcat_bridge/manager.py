import json
from pathlib import Path
from typing import Dict, List, Union
from .utils.Id2IdList import (Id2IdList,
                              add_first2second,
                              add_first2seconds,
                              add_firsts2second,
                              add_firsts2seconds,
                              del_first4second,
                              del_first4seconds,
                              del_firsts4second,
                              del_firsts4seconds)

SaveModel = Dict[str, Id2IdList]


class RelationManager:
    __path: Path
    __staff_id2group_list: Id2IdList
    __group_id2subscribers: Id2IdList

    def __init__(self, path: Path = Path() / 'data' / 'bridge' / 'relation.json'):
        super(RelationManager, self).__init__()
        self.__path = path
        self.__staff_id2group_list: Id2IdList = {}
        self.__group_id2subscribers: Id2IdList = {}
        self.__load()

    def __load(self):
        try:
            with open(self.__path, 'r', encoding='utf-8') as file:
                load: SaveModel = json.load(file)
                self.__staff_id2group_list = load['staff2groups']
                self.__group_id2subscribers = load['group2subscribers']
        except KeyError:
            self.__staff_id2group_list = {}
            self.__group_id2subscribers = {}

    def __dump(self):
        with open(self.__path, 'w', encoding='utf-8') as file:
            save: SaveModel = {'staff2groups': self.__staff_id2group_list,
                               'group2subscribers': self.__group_id2subscribers}
            json.dump(save, file, ensure_ascii=False, indent=2)

    def is_superuser(self, userid: Union[int, str]) -> bool:
        return int(userid) in self.__staff_id2group_list.keys()

    def get_superuser_groups(self, userid: Union[int, str]) -> List[int]:
        if self.is_superuser(userid):
            return self.__staff_id2group_list[int(userid)]
        else:
            return []

    def get_subscribers(self, group_id: Union[int, str]) -> List[int]:
        if int(group_id) in self.__group_id2subscribers.keys():
            return self.__group_id2subscribers[int(group_id)]
        else:
            return []

    def add_staff2group(self, userid: Union[int, str], group_id: Union[int, str]):
        add_first2second(self.__staff_id2group_list, userid, group_id)
        self.__dump()

    def add_staff2groups(self, userid: Union[int, str], group_ids: List[Union[int, str]]):
        add_first2seconds(self.__staff_id2group_list, userid, group_ids)
        self.__dump()

    def add_staffs2group(self, user_ids: List[Union[int, str]], group_id: Union[int, str]):
        add_firsts2second(self.__staff_id2group_list, user_ids, group_id)
        self.__dump()

    def add_staffs2groups(self, user_ids: List[Union[int, str]], group_ids: List[Union[int, str]]):
        add_firsts2seconds(self.__staff_id2group_list, user_ids, group_ids)
        self.__dump()

    def del_staff4group(self, userid: Union[int, str], group_id: Union[int, str]):
        del_first4second(self.__staff_id2group_list, userid, group_id)
        self.__dump()

    def del_staff4groups(self, userid: Union[int, str], group_ids: List[Union[int, str]]):
        del_first4seconds(self.__staff_id2group_list, userid, group_ids)
        self.__dump()

    def del_staffs4group(self, user_ids: List[Union[int, str]], group_id: Union[int, str]):
        del_firsts4second(self.__staff_id2group_list, user_ids, group_id)
        self.__dump()

    def del_staffs4groups(self, user_ids: List[Union[int, str]], group_ids: List[Union[int, str]]):
        del_firsts4seconds(self.__staff_id2group_list, user_ids, group_ids)
        self.__dump()
        