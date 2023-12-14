class Car:
    def __init__(self, engine_type, model_type, colour, tank_capacity):
        self.engine_type = engine_type
        self.model_type = model_type
        self.colour = colour
        self.tank_capacity = tank_capacity

class M01(Car):
    def __init__(self, model_type, color, tank_capacity):
        super().__init__('Gasoline', model_type, color, tank_capacity)

class M02(Car):
    def __init__(self, color, tank_capacity):
        super().__init__('Gasoline', 'Automatic', color, tank_capacity)

class M03(Car):
    def __init__(self, color, battery_capacity):
        super().__init__('Electric', 'Automatic', color, 0)
        self.battery_capacity = battery_capacity

class M04(Car):
    def __init__(self, color, tank_capacity, battery_capacity):
        super().__init__('Hybrid', 'Automatic', color, tank_capacity)
        self.battery_capacity = battery_capacity

class Car:
    def __init__(self, model_code, engine_type, model_type, color, tank_capacity, Battery_capacity):
        self.model_code = model_code
        self.engine_type = engine_type
        self.model_type = model_type
        self.color = color
        self.tank_capacity = tank_capacity
        self.Battery_capacity = Battery_capacity

# information of features
class CarDatabase:
    def __init__(self):
        self.car_data = {}

    def add_car(self, model_code, engine_type, model_type, color, tank_capacity, Battery_capacity):
        self.car_data[model_code] = Car(model_code, engine_type, model_type, color, tank_capacity, Battery_capacity)

    def get_car_details(self, model_code):
        if model_code in self.car_data:
            return self.car_data[model_code]
        else:
            return None


def main():
    car_db = CarDatabase()

    car_db.add_car("M01", "Gasoline", "Manual", "Blue", "50", "40")
    car_db.add_car("M02", "Gasoline", "Automatic", " Black", "60", "50k")
    car_db.add_car("M03", "Electric", "Automatic", "Red ", "60", "50")
    car_db.add_car("M04", "Gasoline and Electric", "Automatic", "White", "50", "40")

    while True:
        try:
            model_code = input("Enter the model code : ")

            if model_code.lower() == "exit":
                print("Exiting the program.")
                break

            car = car_db.get_car_details(model_code)
            if car:
                print(f"Model Code: {car.model_code}")
                print(f"Model Type: {car.model_type}")
                print(f"Engine Type: {car.engine_type}")

                if "Electric" in car.engine_type:
                    car.color = input("Enter car color: ")
                    car.tank_capacity = "N/A"
                else:
                    car.color = input("Enter car color: ")
                    car.tank_capacity = input("Enter tank capacity: ")

                print(f"Car Color: {car.color}")
                print(f"Tank Capacity: {car.tank_capacity}")
            else:
                print("Car not found. Please enter a valid model code.")
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt detected. Exiting the program.")
            break

    while True:
        model_code = input("Enter the model code : ")

        car = car_db.get_car_details(model_code)
        if car:
            print(f"Car Model: {car.model_code}")
            print(f"Engine Type : {car.engine_type}")
            print(f"Model Type: {car.model_type}")
            print(f"Car Color: {car.color}")
            print(f"Tank Capacity: {car.tank_capacity} liters")
            print(f"Battery Capacity: {car.Battery_capacity} kwh")
        else:
            print("Car not found. Please enter a valid model code.")


if __name__ == "__main__":
    main()