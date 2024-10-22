class Eagle:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        return f"{self.name} says squawk!"

    def __str__(self):
        return f"Dog: {self.name}, Breed: {self.breed}"