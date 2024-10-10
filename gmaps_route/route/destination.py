from __future__ import annotations

from typing import Optional

from gmaps_route.nodes.abc_node import ABCNode
from gmaps_route.nodes.node import Node
from gmaps_route.route.exceptions import RouteException
from gmaps_route.route.node_item import ABCNodeItem
from gmaps_route.route.route_point import RoutePoint
from gmaps_route.route.subdestination import Subdestination


class Destination(ABCNodeItem, RoutePoint):

    class Builder:

        def __init__(self):
            self._latitude: Optional[float] = None
            self._longitude: Optional[float] = None
            self._subdestinations: list[Subdestination] = []

        def latitude(self, latitude: float) -> Destination.Builder:
            self._latitude = latitude
            return self

        def longitude(self, longitude: float) -> Destination.Builder:
            self._longitude = longitude
            return self

        def add_subdestination(
            self, subdestination: Subdestination
        ) -> Destination.Builder:
            self._subdestinations.append(subdestination)
            return self

        def build(self) -> Destination:
            if self._latitude is None or self._longitude is None:
                raise RouteException("Latitude and longitude are required.")
            return Destination(self._latitude, self._longitude, self._subdestinations)

    def __init__(
        self,
        latitude: float,
        longitude: float,
        subdestinations: list[Subdestination] = [],
    ):
        super(Destination, self).__init__(latitude, longitude)

        lat_lon_node = Node(2, [self.longitude, self.latitude])

        destination_nodes: list[ABCNode] = [lat_lon_node]
        for subdestination in reversed(subdestinations):
            destination_nodes.append(subdestination.node)

        self._node = Node(1, destination_nodes)

    @property
    def node(self) -> Node:
        return self._node
