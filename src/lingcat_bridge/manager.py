import json
from pathlib import Path
from typing import Dict, List, Union

Id2IdList = Dict[int, List[int]]
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

    def add_superuser2group(self, userid: Union[int, str], group_id: Union[int, str]):
        userid = int(userid)
        group_id = int(group_id)
        if userid not in self.__staff_id2group_list:
            self.__staff_id2group_list[userid] = []
        self.__staff_id2group_list[userid].append(group_id)
        self.__dump()

    def add_superuser2groups(self, userid: Union[int, str], group_ids: List[Union[int, str]]):
        userid = int(userid)
        if not self.is_superuser(userid):
            self.__staff_id2group_list[userid] = []
        for group_id in group_ids:
            group_id = int(group_id)
            self.__staff_id2group_list[userid].append(group_id)
        self.__dump()

    def add_superusers2group(self, user_ids: List[Union[int, str]], group_id: Union[int, str]):
        for userid in user_ids:
            self.add_superuser2group(userid, group_id)
        return

    def add_superusers2groups(self, user_ids: List[Union[int, str]], group_ids: List[Union[int, str]]):
        for userid in user_ids:
            self.add_superuser2groups(userid, group_ids)
        return

    def del_superuser4group(self, userid: Union[int, str], group_id: Union[int, str]):
        userid = int(userid)
        group_id = int(group_id)
        if not self.is_superuser(userid):
            return
        if group_id in self.__staff_id2group_list[userid]:
            self.__staff_id2group_list[userid].remove(group_id)
            self.__dump()
        else:
            return

    def del_superuser4groups(self, userid: Union[int, str], group_ids: List[Union[int, str]]):
        userid = int(userid)
        if not self.is_superuser(userid):
            return
        for group_id in group_ids:
            group_id = int(group_id)
            if group_id in self.__staff_id2group_list[userid]:
                self.__staff_id2group_list[userid].remove(group_id)
        self.__dump()
        return

    def del_superusers4group(self, user_ids: List[Union[int, str]], group_id: Union[int, str]):
        for userid in user_ids:
            self.del_superuser4group(userid, group_id)
        return

    def del_superusers4groups(self, user_ids: List[Union[int, str]], group_ids: List[Union[int, str]]):
        for userid in user_ids:
            self.del_superuser4groups(userid, group_ids)
        return

    def add_subscriber2group(self, subscriber: Union[int, str], group_id:Union[int, str]):
