from abc import ABC, abstractmethod

from gmaps_route.nodes.node import Node


class ABCNodeItem(ABC):

    @property
    @abstractmethod
    def node(self) -> Node:
        pass
