from __future__ import annotations

from gmaps_route.nodes.abc_node import ABCNode


class Node(ABCNode):

    class NodeData(ABCNode.ABCData):
        NODE_TYPE = ABCNode.ABCData.DataType.M

        def __init__(self, id: int, node: Node):
            super(Node.NodeData, self).__init__(id, Node.NodeData.NODE_TYPE)
            self._parent = node

        @property
        def value(self) -> str:
            return str(len(self._parent.flatten()) - 1)

    def __init__(self, id: int, children: list[ABCNode] = []):
        self._children = children
        self._data = Node.NodeData(id, self)

    @property
    def children(self) -> list[ABCNode]:
        return self._children

    @property
    def data(self) -> Node.NodeData:
        return self._data
