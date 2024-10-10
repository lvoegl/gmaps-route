from __future__ import annotations

import re

from abc import ABC, abstractmethod
from enum import Enum


class ABCNode(ABC):

    class ABCData(ABC):

        __data_regex = re.compile("^(\d+)([a-z])(.+)$")

        class DataType(str, Enum):

            # TODO: find out what these stand for - currently I have no idea
            D = "d"
            S = "s"
            M = "m"
            E = "e"
            B = "b"

            def __str__(self):
                return self.value

        def __init__(self, id: int, type: DataType):
            self._id = id
            self._type = type

        @property
        def id(self) -> int:
            return self._id

        @property
        def type(self) -> DataType:
            return self._type

        @property
        @abstractmethod
        def value(self) -> str:
            pass

    @property
    @abstractmethod
    def children(self) -> list[ABCNode]:
        pass

    @property
    @abstractmethod
    def data(self) -> ABCData:
        pass

    def has_children(self) -> bool:
        return len(self.children) > 0

    def add_child(self, child: ABCNode) -> None:
        self.children.append(child)

    def flatten(self) -> list[ABCNode]:
        def _flatten(node: ABCNode, nodes: list[ABCNode] = []) -> None:
            nodes.append(node)
            for child in node.children:
                _flatten(child, nodes)

        nodes: list[ABCNode] = []
        _flatten(self, nodes)
        return nodes

    def __str__(self) -> str:
        return f"{str(self.data.id)}{self.data.type}{self.data.value}"
