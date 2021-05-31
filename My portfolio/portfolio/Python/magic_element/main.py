import random


class Water:
    pass

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Ether):
            return Tsunami()


class Air:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Water):
            return Storm()
        elif isinstance(other, Ether):
            return Wind()


class Fire:
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Ether):
            return Radiance()


class Earth:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Ether):
            return Earthquake()


class Ether:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Radiance()
        elif isinstance(other, Water):
            return Tsunami()
        elif isinstance(other, Air):
            return Wind()
        elif isinstance(other, Earth):
            return Earthquake()


class Storm:
    pass


class Steam:
    pass


class Dirt:
    pass


class Lightning:
    pass


class Dust:
    pass


class Lava:
    pass


class Tsunami:
    pass


class Wind:
    pass


class Radiance:
    pass


class Earthquake:
    pass


elements = [Water(), Air(), Fire(), Earth(), Ether()]
new_element_1 = random.choice(elements)
new_element_2 = random.choice(elements)
print(new_element_1 + new_element_2)
