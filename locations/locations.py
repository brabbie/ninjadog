class Location:
    def __init__(self, name):
        self.name = name

class LocalPawb(Location):
    def __init__(self):
        super().__init__('Local Pawb')
        self.dogtails = ["The Pink Poodle", "The Salty Dog", "Pupsi", "Puppuccino", "Muttgarita", "The GreyHound"]
        self.food = ["Pawsta", "Pupperoni", "The Hot Dog", "Pupcorn"]

class PawtyPark(Location):
    def __init__(self):
        super().__init__("Pawty Park")



if __name__ == "__main__":
    x = Location("Dogo")
    print(x.name)
    y = LocalPawb()
    print(y.dogtails)
