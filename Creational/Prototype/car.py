import copy


class Car:
    def __init__(self, name="Skylark", color="red", model="sedan"):
        self.name = name
        self.color = color
        self.model = model

    def __str__(self):
        return "{} | {} | {}".format(self.name, self.color, self.model)


class Prototype():
    def __init__(self):
        self.objects = {}

    def register(self, name, obj):
        self.objects[name] = obj

    def unregister(self, name):
        del self.objects[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self.objects[name])
        obj.__dict__.update(attr)
        return obj
