from abc import ABC

from homework_02 import exceptions


class Vehicle(ABC):
    weight = 0
    fuel = 0
    fuel_consumption = 0
    started = False

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError("Топливо отсутсвует!")

    def move(self, distance):
        if self.fuel_consumption * distance <= self.fuel:
            self.fuel -= self.fuel_consumption * distance
        else:
            raise exceptions.NotEnoughFuel(
                f"Топлива хватит только на {self.fuel / self.fuel_consumption} км"
            )
