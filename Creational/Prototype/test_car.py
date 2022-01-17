from Creational.Prototype.car import Car, Prototype


class TestCar:
    def test_car(self):
        c = Car()
        prototype = Prototype()
        prototype.register("Skylark", c)

        c1 = prototype.clone("Skylark", color='green')
        assert isinstance(c1, Car) == True
        assert c1.color == "green"