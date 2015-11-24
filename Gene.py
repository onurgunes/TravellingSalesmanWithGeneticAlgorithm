__author__ = 'OnurGunes'


class Gene(object):
    """
        Class That Represent Gene
    """

    name = ""
    latitude = 0
    longitude = 0

    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude