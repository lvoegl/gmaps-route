# GMaps Route

GMaps Route allows you to create routes for Google Maps offline directly in Python.
The project lets you create a route between two locations, add intermediate destinations and specify waypoints (subdestinations) to route along.

A simple and more complex example can be found in the [examples/](./examples) directory.

## Installation
`pip install gmaps-route`

## Examples
### Simple
```
python examples/simple.py
https://www.google.com/maps/dir/data=!4m9!4m8!1m3!2m2!1d8.6821267!2d50.1109221!1m3!2m2!1d11.5819805!2d48.1351253
```
Will print the URL to a simple route from Munich (start) to Frankfurt (end).
![Image of simple route](examples/simple.png)

### Complex
```
python examples/large.py
https://www.google.com/maps/dir/data=!3m1!1e3!4m26!4m25!1m7!2m2!1d8.6821267!2d50.1109221!3m3!1m2!1d8.4401422!2d49.4816004!1m11!2m2!1d9.1829321!2d48.7758459!3m3!1m2!1d9.9998080!2d48.4040736!3m3!1m2!1d11.4316520!2d48.1276310!1m3!2m2!1d11.5819805!2d48.1351253!3e0
```
Will print the URL to a route from Munich (start) to Stuttgart (intermediate) to Frankfurt (end).
It also adds subdestinations (waypoints to route-along) between destinations.
Note that these subdestinations between destinations always have to be added to the later destination of the two.
This route also configures the map type as 'Satellite' and transportation type as 'Car'.
![Image of complex route](examples/large.png)
