from gmaps_route.nodes.abc_node import ABCNode
from gmaps_route.nodes.leaf import Leaf


class RoutePoint:
    def __init__(self, latitude: float, longitude: float):
        self._longitude = Leaf(
            1, ABCNode.ABCData.DataType.D, RoutePoint._format_coordinate(longitude)
        )
        self._latitude = Leaf(
            2, ABCNode.ABCData.DataType.D, RoutePoint._format_coordinate(latitude)
        )

    @staticmethod
    def _format_coordinate(coord: float) -> str:
        return f"{coord:.7f}"

    @property
    def latitude(self) -> Leaf:
        return self._latitude

    @property
    def longitude(self) -> Leaf:
        return self._longitude
