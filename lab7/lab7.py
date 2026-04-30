
class Vehicle:
    def __init__(self, vid, model, year):
        self.vid = vid
        self.model = model
        self.year = year

    def __str__(self):
        text = "VID: "
        text = text + self.vid
        text = text + " | "
        text = text + self.model
        text = text + " ("
        text = text + str(self.year)
        text = text + ")"
        return text

    def __eq__(self, other):
        return self.vid == other.vid

    def is_new(self, n):
        return (2026 - self.year) <= n



class Car(Vehicle):
    def __init__(self, vid, model, year, fuel_type, doors):
        Vehicle.__init__(self, vid, model, year)
        self.fuel_type = fuel_type
        self.doors = doors

    def __str__(self):
        text = "[Car] VID: "
        text = text + self.vid
        text = text + " | "
        text = text + self.model
        text = text + " ("
        text = text + str(self.year)
        text = text + ") | Fuel: "
        text = text + self.fuel_type
        text = text + " | "
        text = text + str(self.doors) + " Doors"
        return text



class Truck(Vehicle):
    def __init__(self, vid, model, year, max_load, axles):
        Vehicle.__init__(self, vid, model, year)
        self.max_load = max_load
        self.axles = axles

    def __str__(self):
        text = "[Truck] VID: "
        text = text + self.vid
        text = text + " | "
        text = text + self.model
        text = text + " ("
        text = text + str(self.year)
        text = text + ") | Load: "
        text = text + str(self.max_load)
        text = text + "kg | "
        text = text + str(self.axles) + " Axles"
        return text



class Motorcycle(Vehicle):
    def __init__(self, vid, model, year, engine_cc, type):
        Vehicle.__init__(self, vid, model, year)
        self.engine_cc = engine_cc
        self.type = type

    def __str__(self):
        text = "[Motorcycle] VID: "
        text = text + self.vid
        text = text + " | "
        text = text + self.model
        text = text + " ("
        text = text + str(self.year)
        text = text + ") | Eng: "
        text = text + str(self.engine_cc)
        text = text + "cc | Type: "
        text = text + self.type
        return text



def save_fleet_to_file(vehicles, filename):
    f = open(filename, "w")

    for v in vehicles:
        if isinstance(v, Car):
            line = "Car," + v.vid + "," + v.model + "," + str(v.year) + "," + v.fuel_type + "," + str(v.doors) + "\n"
        elif isinstance(v, Truck):
            line = "Truck," + v.vid + "," + v.model + "," + str(v.year) + "," + str(v.max_load) + "," + str(v.axles) + "\n"
        else:
            line = "Motorcycle," + v.vid + "," + v.model + "," + str(v.year) + "," + str(v.engine_cc) + "," + v.type + "\n"

        f.write(line)

    f.close()



def load_fleet_from_file(filename):
    lst = []
    f = open(filename, "r")

    for line in f:
        parts = line.strip().split(",")

        if parts[0] == "Car":
            obj = Car(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5]))
        elif parts[0] == "Truck":
            obj = Truck(parts[1], parts[2], int(parts[3]), int(parts[4]), int(parts[5]))
        else:
            obj = Motorcycle(parts[1], parts[2], int(parts[3]), int(parts[4]), parts[5])

        lst.append(obj)

    f.close()
    return lst



vehicles = []
vehicles.append(Car("V001", "Tesla Model 3", 2023, "Electric", 4))
vehicles.append(Car("V002", "Toyota Corolla", 2018, "Petrol", 4))
vehicles.append(Truck("T101", "Volvo FH16", 2019, 25000, 6))
vehicles.append(Truck("T102", "Mercedes Actros", 2021, 18000, 4))
vehicles.append(Motorcycle("M301", "Yamaha R1", 2024, 998, "Sport"))
vehicles.append(Motorcycle("M302", "Harley Davidson", 2015, 1200, "Cruiser"))

save_fleet_to_file(vehicles, "fleet.txt")

print("Loading fleet data from 'fleet.txt'...")
loaded_vehicles = load_fleet_from_file("fleet.txt")
print(str(len(loaded_vehicles)) + " vehicles loaded successfully.\n")

print("--- All Vehicles ---")
for i in loaded_vehicles:
    print(i)

print("\n--- Recent Vehicles (Last 4 Years) ---")
for i in loaded_vehicles:
    if i.is_new(4):
        print(i)

print("\n--- Electric Cars Only ---")
for i in loaded_vehicles:
    if isinstance(i, Car) and i.fuel_type == "Electric":
        print(i)
