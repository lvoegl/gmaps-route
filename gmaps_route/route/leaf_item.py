from abc import ABC, abstractmethod

from gmaps_route.nodes.leaf import Leaf


class ABCLeafItem(ABC):

    @property
    @abstractmethod
    def leaf(self) -> Leaf:
        pass
