from Creational.Singleton.singleton import Singleton


class TestSigleton:

    def test_oone(self):
        obj1 = Singleton()
        obj1.add_some_data(HTTP = "Hyper Text Markup Language")
        obj2 = Singleton()

        assert obj1 == obj2
        assert obj2.data == {"HTTP": "Hyper Text Markup Language"}