import os
import sys


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# The above lines are only required to run in the repository's examples directory

from gmaps_route.route.destination import Destination
from gmaps_route.route.map import Map
from gmaps_route.route.route import Route
from gmaps_route.route.subdestination import Subdestination
from gmaps_route.route.transportation import Transportation


route_map = Map(Map.Type.SATELLITE)
transportation = Transportation(Transportation.Type.CAR)

start = Destination.Builder().latitude(48.1351253).longitude(11.5819805).build()
intermediate = (
    Destination.Builder()
    .latitude(48.7758459)
    .longitude(9.1829321)
    .add_subdestination(
        # note that subdestinations between 'start' and 'intermediate' must be added to 'intermediate'
        Subdestination.Builder()
        .latitude(48.127631)
        .longitude(11.431652)
        .build()
    )
    .add_subdestination(
        Subdestination.Builder().latitude(48.4040736).longitude(9.999808).build()
    )
    .build()
)

end = (
    Destination.Builder()
    .latitude(50.1109221)
    .longitude(8.6821267)
    .add_subdestination(
        Subdestination.Builder().latitude(49.4816004).longitude(8.4401422).build()
    )
    .build()
)

route = (
    Route.Builder()
    .map(route_map)
    .transportation(transportation)
    .add_destination(start)
    .add_destination(intermediate)
    .add_destination(end)
    .build()
)
print(route.url)
