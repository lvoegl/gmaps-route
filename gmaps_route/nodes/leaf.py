from __future__ import annotations

from gmaps_route.nodes.abc_node import ABCNode


class Leaf(ABCNode):

    class LeafData(ABCNode.ABCData):

        def __init__(self, id: int, type: ABCNode.ABCData.DataType, value: str):
            super(Leaf.LeafData, self).__init__(id, type)
            self._value = value

        @property
        def value(self) -> str:
            return self._value

    def __init__(self, id: int, type: ABCNode.ABCData.DataType, value: str):
        self._children: list[ABCNode] = []
        self._data = Leaf.LeafData(id, type, value)

    @property
    def children(self) -> list[ABCNode]:
        return self._children

    @property
    def data(self) -> ABCNode.ABCData:
        return self._data
