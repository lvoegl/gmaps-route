from __future__ import annotations

from enum import Enum

from gmaps_route.nodes.abc_node import ABCNode
from gmaps_route.nodes.leaf import Leaf
from gmaps_route.nodes.node import Node
from gmaps_route.route.node_item import ABCNodeItem


class Map(ABCNodeItem):

    class Type(int, Enum):
        MAP = 1
        SATELLITE = 3

    def __init__(self, map_type: Map.Type):
        if map_type == Map.Type.SATELLITE:
            data_type = ABCNode.ABCData.DataType.E
            data_id = 1
        else:
            data_type = ABCNode.ABCData.DataType.B
            data_id = 4

        map_leaf = Leaf(data_id, data_type, str(int(map_type)))
        self._map = Node(3, [map_leaf])

    @property
    def node(self) -> Node:
        return self._map
