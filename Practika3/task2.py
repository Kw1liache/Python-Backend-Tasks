from datetime import date


class Vehicle:
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    def description(self) -> str:
        return f"Транспортное средство: {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int) -> None:
        super().__init__(make, model)
        self.year = year

    def description(self) -> str:
        return f"Автомобиль: {self.year} {self.make} {self.model}"


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, engine_volume: int) -> None:
        super().__init__(make, model)
        self.engine_volume = engine_volume

    def description(self) -> str:
        return (
            f"Мотоцикл: {self.make} {self.model}, "
            f"объём двигателя {self.engine_volume} куб. см"
        )


class Bicycle(Vehicle):
    def __init__(self, make: str, model: str, bicycle_type: str) -> None:
        super().__init__(make, model)
        self.bicycle_type = bicycle_type

    def description(self) -> str:
        return f"Велосипед: {self.make} {self.model}, тип: {self.bicycle_type}"


if __name__ == "__main__":
    vehicles = [
        Car("Toyota", "Corolla", date.today().year),
        Motorcycle("Yamaha", "MT-07", 689),
        Bicycle("Trek", "Marlin", "горный"),
    ]

    for vehicle in vehicles:
        print(vehicle.description())
