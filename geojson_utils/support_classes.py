from typing import Tuple, List


class GeoCoord:
    def __init__(self, coord: List):
        self.lon = coord[0]
        self.lat = coord[1]

    def __eq__(self, other) -> bool:
        return self.lon == other.lon and self.lat == other.lat

    def __hash__(self) -> int:
        return hash(int(self.lon * 1000000000 + self.lat * 1000000))

    def __lt__(self, other):
        if (other.lat - self.lat) == 0:
            return other.lon < self.lon
        return ((other.lon - self.lon) / (other.lat - self.lat)) < 0

    def __gt__(self, other):
        return not self.__lt__(other)
