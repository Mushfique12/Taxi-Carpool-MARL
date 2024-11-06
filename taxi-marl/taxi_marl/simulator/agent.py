class Driver:
    def __init__(self):
        self.online = True
        self.onservice = False
        self.order = None     # the order this driver is serving
        self.node = None      # the node that contain this driver.
        self.city_time = 0  # track the current system time

        # private
        self._driver_id = driver_id  # unique driver id.