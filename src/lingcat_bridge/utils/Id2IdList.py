from typing import Dict, List, Union

Id2IdList = Dict[int, List[int]]


def add_first2second(it: Id2IdList, first: Union[int, str], second: Union[int, str]):
    first = int(first)
    second = int(second)
    if first not in it.keys():
        it[first] = []
    it[first].append(second)


def add_first2seconds(it: Id2IdList, first: Union[int, str], seconds: List[Union[int, str]]):
    first = int(first)
    if first not in it.keys():
        it[first] = []
    for second in seconds:
        second = int(second)
        it[first].append(second)


def add_firsts2second(it: Id2IdList, firsts: List[Union[int, str]], second: Union[int, str]):
    for first in firsts:
        add_first2second(it, first, second)


def add_firsts2seconds(it: Id2IdList, firsts: List[Union[int, str]], seconds: List[Union[int, str]]):
    for first in firsts:
        add_first2seconds(it, first, seconds)


def del_first4second(it: Id2IdList, first: Union[int, str], second: Union[int, str]):
    first = int(first)
    second = int(second)
    if first not in it.keys():
        return
    if second in it[first]:
        it[first].remove(second)
    else:
        return


def del_first4seconds(it: Id2IdList, first: Union[int, str], seconds: List[Union[int, str]]):
    first = int(first)
    if first not in it.keys():
        return
    for second in seconds:
        second = int(second)
        if second in it[first]:
            it[first].remove(second)


def del_firsts4second(it: Id2IdList, firsts: List[Union[int, str]], second: Union[int, str]):
    for first in firsts:
        del_first4second(it, first, second)


def del_firsts4seconds(it: Id2IdList, firsts: List[Union[int, str]], seconds: List[Union[int, str]]):
    for first in firsts:
        del_first4seconds(it, first, seconds)
