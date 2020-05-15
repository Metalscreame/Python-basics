class GeoLocation:
    def __init__(self, lat, long):
        """init class from lat,long as radians"""

    @classmethod
    def from_degrees(cls, dlat, dlong):
        """creat `cls` from lat,long in degrees """
        return cls(float(dlat), int(dlong))

    @classmethod
    def fromRadians(cls, lat, long):  # just in case
        return cls(lat, long)

    def __some_private_method(self):
        print('im very private')

    def some_method(self):
        print("some")

    @staticmethod
    def some_method():
        print("some")


# obj = GeoLocation.from_degrees(10, 20)  # returns a new geoLocation object
# print(type(obj))
# obj._some_private - cant do that

#obj._GeoLocation__some_private_method()