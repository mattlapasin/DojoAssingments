class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayinfo(self)
        print "price: " +str.(self.price)
        print "maximum speed: " +str.(self.max_speed)
        print "miles: " +str.(self.miles)
        return self

    def ride(self)
        print "riding"
        self.miles += 10
        return self

    def reverse(self)
        if self.miles > 4
            print "Reversing"
            self.miles -= 5
        else:
            self.miles -=0
        return self

#Create instance 1 = ride 3 times, reverse 1 time, and display info
bike1 = Bike(200, "25mph")
bike1.displayinfo().ride().ride().ride().reverse().displayinfo()
# Create instance 2 = ride 2 times, reverse 2 times, and display info
bike2 = Bike(200, "25mph")
bike2.displayinfo().ride().ride().reverse().reverse().displayinfo()
# Create instance 3 = reverse 3 times and display info
bike3 = Bike(200, "25mph")
bike3.displayinfo().reverse().reverse().reverse().displayinfo()
