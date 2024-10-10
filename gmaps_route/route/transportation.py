from __future__ import annotations

from enum import Enum

from gmaps_route.nodes.abc_node import ABCNode
from gmaps_route.nodes.leaf import Leaf
from gmaps_route.route.leaf_item import ABCLeafItem


class Transportation(ABCLeafItem):

    class Type(int, Enum):
        CAR = 0
        BIKE = 1
        FOOT = 2
        TRANSIT = 3
        FLIGHT = 4

    def __init__(self, transportation_type: Transportation.Type):
        self._transportation = Leaf(
            3, ABCNode.ABCData.DataType.E, str(int(transportation_type))
        )

    @property
    def leaf(self) -> Leaf:
        return self._transportation
