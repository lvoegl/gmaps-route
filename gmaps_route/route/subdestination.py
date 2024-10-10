from __future__ import annotations

from gmaps_route.nodes.node import Node
from gmaps_route.route.exceptions import RouteException
from gmaps_route.route.node_item import ABCNodeItem
from gmaps_route.route.route_point import RoutePoint


class Subdestination(ABCNodeItem, RoutePoint):

    class Builder:

        def __init__(self):
            self._latitude: Optional[float] = None
            self._longitude: Optional[float] = None

        def latitude(self, latitude: float) -> Subdestination.Builder:
            self._latitude = latitude
            return self

        def longitude(self, longitude: float) -> Subdestination.Builder:
            self._longitude = longitude
            return self

        def build(self) -> Subdestination:
            if self._latitude is None or self._longitude is None:
                raise RouteException("Latitude and longitude are required.")
            return Subdestination(self._latitude, self._longitude)

    def __init__(self, latitude: float, longitude: float):
        super(Subdestination, self).__init__(latitude, longitude)

        lat_lon_node = Node(1, [self.longitude, self.latitude])
        self._node = Node(3, [lat_lon_node])

    @property
    def node(self) -> Node:
        return self._node
