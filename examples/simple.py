import os
import sys


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# The above lines are only required to run in the repository's examples directory

from gmaps_route.route.destination import Destination
from gmaps_route.route.map import Map
from gmaps_route.route.route import Route
from gmaps_route.route.subdestination import Subdestination
from gmaps_route.route.transportation import Transportation


start = Destination.Builder().latitude(48.1351253).longitude(11.5819805).build()
end = Destination.Builder().latitude(50.1109221).longitude(8.6821267).build()

route = Route.Builder().add_destination(start).add_destination(end).build()
print(route.url)
