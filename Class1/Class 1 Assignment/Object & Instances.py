"""Object: Smartphone
Class: Mobile Device
Instances:
 iPhone 15 Pro, 256GB, Space Black
 Samsung Galaxy S24, 128GB, Titanium Gray
"""
class Smartphone:
    def __init__(self, model, storage, color):
        self.model = model
        self.storage = storage
        self.color = color

"""Object: Bicycle
Class: Vehicle
Instances:
 Red Mountain Bike, 21 gears, Aluminum frame
 Blue Road Bike, 18 gears, Carbon frame
"""
class Bicycle:
    def __init__(self, type, gears, frame_material):
        self.type = type
        self.gears = gears
        self.frame_material = frame_material

"""Object: Coffee
Class: Beverage
Instances:
 Large Latte, Oat Milk, Extra Shot
 Medium Cappuccino, Almond Milk, Decaf
"""
class Coffee:
    def __init__(self, size, milk_type, special_requests):
        self.size = size
        self.milk_type = milk_type
        self.special_requests = special_requests

"""Object: Guitar
Class: Musical Instrument
Instances:
 Fender Stratocaster, Electric, 6 strings
 Yamaha Acoustic, Steel strings, Natural finish
"""
class Guitar:
    def __init__(self, brand, guitar_type, strings):
        self.brand = brand
        self.guitar_type = guitar_type
        self.strings = strings

"""Object: Watch
Class: Accessory
Instances:
 Rolex Submariner, Gold, Waterproof 300m
 Apple Watch Series 9, Space Gray, GPS + Cellular
"""
class Watch:
    def __init__(self, brand, material, features):
        self.brand = brand
        self.material = material
        self.features = features

#INSTANCES TO OBJECTS I CREATED ABOVE
phone1 = Smartphone("iPhone 15 Pro", "256GB", "Space Black")
phone2 = Smartphone("Samsung Galaxy S24", "128GB", "Titanium Gray")
phone3 = Smartphone("Google Pixel 8", "256GB", "Hazel")
phone4 = Smartphone("OnePlus 12", "512GB", "Silky Black")
phone5 = Smartphone("Xiaomi 14", "128GB", "White")

bike1 = Bicycle("Mountain Bike", "21 gears", "Aluminum")
bike2 = Bicycle("Road Bike", "18 gears", "Carbon")
bike3 = Bicycle("Hybrid Bike", "24 gears", "Steel")
bike4 = Bicycle("BMX Bike", "Single gear", "Chromoly")
bike5 = Bicycle("Electric Bike", "7 gears", "Aluminum")

coffee1 = Coffee("Large", "Regular Milk", "No Sugar")
coffee2 = Coffee("Medium", "No Milk", "With Sugar")
coffee3 = Coffee("Small", "Regular Milk", "Extra Sugar")
coffee4 = Coffee("Large", "No Milk", "No Sugar")
coffee5 = Coffee("Medium", "Regular Milk", "Normal Sugar")

guitar1 = Guitar("Fender", "Electric", "6 strings")
guitar2 = Guitar("Yamaha", "Acoustic", "Steel strings")
guitar3 = Guitar("Gibson", "Electric", "6 strings")
guitar4 = Guitar("Martin", "Acoustic", "Nylon strings")
guitar5 = Guitar("Ibanez", "Electric", "7 strings")

watch1 = Watch("Rolex", "Gold", "Waterproof 300m")
watch2 = Watch("Apple", "Space Gray", "GPS + Cellular")
watch3 = Watch("Omega", "Stainless Steel", "Chronograph")
watch4 = Watch("Casio", "Plastic", "Digital Display")
watch5 = Watch("Tag Heuer", "Titanium", "Automatic Movement")