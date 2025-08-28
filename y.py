import random

class Smartphone:
    
    def __init__(self, brand, model, storage_gb, color):
        
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.color = color
        self._apps_installed = []  # Encapsulated list of installed apps

        print(f"[{self.brand} {self.model}] A new smartphone has been created!")

    def call(self, number):
        
        print(f"[{self.brand} {self.model}] Calling {number}...")

    def take_photo(self):
        
        print(f"[{self.brand} {self.model}] *Click!* Photo taken.")

    def install_app(self, app_name):
        
        if app_name not in self._apps_installed:
            self._apps_installed.append(app_name)
            print(f"[{self.brand} {self.model}] Installing '{app_name}'...")
        else:
            print(f"[{self.brand} {self.model}] '{app_name}' is already installed.")

    def get_installed_apps(self):
        
        return self._apps_installed

    def __str__(self):
        
        return f"{self.color} {self.brand} {self.model} with {self.storage_gb}GB storage"

class GamingSmartphone(Smartphone):
    
    def __init__(self, brand, model, storage_gb, color, refresh_rate_hz, cooling_system_type):
        
        super().__init__(brand, model, storage_gb, color) # Call parent constructor
        self.refresh_rate_hz = refresh_rate_hz
        self.cooling_system_type = cooling_system_type
        print(f"[{self.brand} {self.model}] This is a gaming smartphone with {self.refresh_rate_hz}Hz refresh rate!")

    def play_game(self, game_title):
    
        print(f"[{self.brand} {self.model}] Launching '{game_title}' at {self.refresh_rate_hz}Hz! Enjoy the smooth gameplay!")

    
    def take_photo(self):
        
        print(f"[{self.brand} {self.model}] *Click!* Quick snapshot of my game score taken!")



class Car:
    
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        
        return f"[{self.make} {self.model}] Driving 🚗 down the road."

class Plane:
    
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
    
        return f"[{self.make} {self.model}] Flying ✈️ through the sky."

class Boat:
    
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        
        return f"[{self.make} {self.model}] Sailing  on the water."

# --- Demonstration ---
if __name__ == "__main__":
    print("--- Activity 1: Smartphone Class Demonstration ---")

    
    my_phone = Smartphone("Google", "Pixel 8", 128, "Obsidian")
    mom_phone = Smartphone("Samsung", "Galaxy A54", 256, "Awesome Violet")

    print(my_phone)
    my_phone.call("555-1234")
    my_phone.take_photo()
    my_phone.install_app("Instagram")
    my_phone.install_app("WhatsApp")
    my_phone.install_app("Instagram") 
    print(f"My phone's apps: {my_phone.get_installed_apps()}")

    print("\n--- Gaming Smartphone (Inheritance) Demonstration ---")
    gaming_phone = GamingSmartphone("ASUS", "ROG Phone 7", 512, "Phantom Black", 165, "Vapor Chamber")
    print(gaming_phone)
    gaming_phone.call("555-5678")
    gaming_phone.install_app("Genshin Impact")
    gaming_phone.play_game("Call of Duty Mobile")
    gaming_phone.take_photo() 

    print("\n--- Activity 2: Polymorphism Challenge Demonstration ---")


    vehicles = [
        Car("Honda", "Civic"),
        Plane("Boeing", "747"),
        Car("Tesla", "Model 3"),
        Boat("Yamaha", "WaveRunner"),
        Plane("Airbus", "A380")
    ]

    print("Let's see how our vehicles move:")
    for vehicle in vehicles:
        print(vehicle.move())
