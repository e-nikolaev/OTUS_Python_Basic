"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02 import exceptions
from homework_02.base import Vehicle


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    # def __init__(self, max_cargo, *args, **kwargs):
    #     """
    #     Не работает для тестов, т. к. в тесте max_cargo передается неименованной переменной в конце
    #     super().__init__(*args, **kwargs)
    #     self.max_cargo = max_cargo

    def __init__(self, *args):
        # Для передечи max_cargo последним аргументом
        all_args = tuple(args)
        super().__init__(*all_args[:-1])
        self.max_cargo = all_args[-1]

    def load_cargo(self, load):
        if self.cargo + load <= self.max_cargo:
            self.cargo += load
        else:
            raise exceptions.CargoOverload(
                f"Перегруз. Допустимо {self.max_cargo - self.cargo} кг груза"
            )

    def remove_all_cargo(self):
        current_cargo = self.cargo
        self.cargo = 0
        return current_cargo
