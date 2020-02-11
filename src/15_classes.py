# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE 
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat 
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name
    def description(self):
        return "{} {} {}".format(self.name, self.lat, self.lon)
    def __str__(self):
        return "{} {} {}".format(self.name, self.lat, self.lon)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypoint):
    def __init__(self, lat, lon, name, difficulty, size):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size = size
    def __str__(self):
        return "{}, diff {}, size {}, {}, {}".format(self.name, self.difficulty, self.size,  self.lat, self.lon)        

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

waypoint = Waypoint(41.70505, -121.51521, "Catacombs")
print(waypoint.description())

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

geocache = Geocache(44.052137, -121.41556, "Newberry Views", 1.5, 2)
print("{}, diff {}, size {}, {}, {}".format(geocache.name, geocache.difficulty, geocache.size, geocache.lat, geocache.lon))

# Print it--also make this print more nicely
print(geocache)
