from __future__ import annotations

a = 1
b = 2


class Saiyan:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def __add__(self, other: Saiyan) -> Saiyan:
        return Saiyan(self.name + other.name, self.power + other.power)

    def __str__(self) -> str:
        return f"{self.name} {self.power}"

    def invert(self) -> Saiyan:
        return Saiyan(self.name[::-1], self.power)


class SuperSaiyan(Saiyan):
    def __init__(self, name: str, power: int, level: int) -> None:
        super().__init__(name, power)
        self.level = level

    def xPower(self):
        return self.power * self.level

    def __str__(self) -> str:
        return f"{super().__str__()} | Level: {self.level}"


goku = Saiyan("Goku", 100)
goku100 = SuperSaiyan("Goku", 100, 100)

# print(goku)
print(goku100)
