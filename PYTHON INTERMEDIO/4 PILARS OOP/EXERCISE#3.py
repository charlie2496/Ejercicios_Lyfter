# ==========================================
# MULTIPLE INHERITANCE
#
# Multiple inheritance allows a class
# to inherit from two or more classes.
#
# In this example, an amphibious vehicle
# inherits from Car and Boat.
# ==========================================


class Car:
    def drive(self):
        print("Driving on the road.")

class Boat:
    def sail(self):
        print("Sailing on the water.")

class AmphibiousVehicle(Car, Boat):
    def drive_and_sail(self):
        self.drive()
        self.sail()
