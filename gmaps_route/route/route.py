from __future__ import annotations

from typing import Optional

from gmaps_route.nodes.abc_node import ABCNode
from gmaps_route.nodes.leaf import Leaf
from gmaps_route.nodes.node import Node
from gmaps_route.nodes.root_node import RootNode
from gmaps_route.route.destination import Destination
from gmaps_route.route.exceptions import RouteException
from gmaps_route.route.map import Map
from gmaps_route.route.transportation import Transportation


class Route:

    GMAPS_DATA_URL = "https://www.google.com/maps/dir/data="

    class Builder:

        def __init__(self):
            self._map: Optional[Map] = None
            self._transportation: Optional[Transportation] = None
            self._destinations: list[Destination] = []

        def map(self, map: Optional[Map]) -> Route.Builder:
            self._map = map
            return self

        def transportation(
            self, transportation: Optional[Transportation]
        ) -> Route.Builder:
            self._transportation = transportation
            return self

        def add_destination(self, destination: Destination) -> Route.Builder:
            self._destinations.append(destination)
            return self

        def build(self) -> Route:
            return Route(self._destinations, self._transportation, self._map)

    def __init__(
        self,
        destinations: list[Destination],
        transportation: Optional[Transportation] = None,
        map: Optional[Map] = None,
    ):
        if len(destinations) < 2:
            raise RouteException("At least two destinations required.")

        self._root = RootNode()
        inner_route_node = Node(4)
        route_node = Node(4, [inner_route_node])

        if map is not None:
            self._root.add_child(map.node)

        for destination in reversed(destinations):
            inner_route_node.add_child(destination.node)

        if transportation is not None:
            inner_route_node.add_child(transportation.leaf)

        self._root.add_child(route_node)

    @property
    def data(self) -> str:
        nodes = self._root.flatten()
        return "!".join([str(n) for n in nodes])

    @property
    def url(self) -> str:
        return f"{Route.GMAPS_DATA_URL}{self.data}"
