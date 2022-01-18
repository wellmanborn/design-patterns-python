from Structural.Facade.facade import Facade, Subsystem1, Subsystem2


class TestFacade:

    def test_one(self):

        assert Facade(Subsystem1(), Subsystem2()).operation() == "success!"