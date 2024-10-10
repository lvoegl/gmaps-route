from __future__ import annotations

from gmaps_route.nodes.abc_node import ABCNode


class RootNode(ABCNode):

    class RootData(ABCNode.ABCData):

        @property
        def value(self) -> str:
            return ""

    def __init__(self, children: list[ABCNode] = []):
        self._children = children
        self._data = RootNode.RootData(-1, ABCNode.ABCData.DataType.M)

    @property
    def children(self) -> list[ABCNode]:
        return self._children

    @property
    def data(self) -> RootNode.RootData:
        return self._data

    def __str__(self) -> str:
        return ""
