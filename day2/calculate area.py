class room:
    length=0.0
    breadth=0.0

    def calculateArea(self):
        print("Area of the room:",self.length*self.breadth)
power_room=room()

power_room.length=19.33
power_room.breadth=12.43
power_room.calculateArea()