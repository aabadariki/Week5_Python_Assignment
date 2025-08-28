# Smartphone class with inheritance

class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

    def info(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage"


# Inherited class (Child class)
class SmartphonePro(Smartphone):
    def __init__(self, brand, model, storage, camera):
        super().__init__(brand, model, storage)  # call parent constructor
        self.camera = camera

    def take_photo(self):
        print(f"Taking a photo with {self.camera}MP camera on {self.brand} {self.model}!")


# Example usage
phone1 = Smartphone("Samsung", "Galaxy S22", 128)
print(phone1.info())
phone1.call("08012345678")

phone2 = SmartphonePro("Apple", "iPhone 14 Pro", 256, 48)
print(phone2.info())
phone2.take_photo()
