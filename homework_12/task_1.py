class Transport:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
        
    def start(self):
        print("Starting the engine.")
        
        
class Train(Transport):
    def __init__(self, make, model, year, num_cars):
        super().__init__(make, model, year)
        self.num_cars = num_cars
        
        
    def start(self):
        print("Starting the locomotive.")
        
        
    def whistle(self):
        print("Toot toot!")
        
        
class Airplane(Transport):
    def __init__(self, make, model, year, max_altitude):
        super().__init__(make, model, year)
        self.max_altitude = max_altitude
        
        
    def start(self):
        print("Starting the engines.")
        
        
    def fly(self):
        print("Flying at", self.max_altitude, "feet.")
