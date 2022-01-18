class Subsystem1:
    """
        The Subsystem can accept requests either from the facade or client directly.
        In any case, to the Subsystem, the Facade is yet another client, and it's
        not a part of the Subsystem.
        """
    def operation1(self) -> str:
        return "Subsystem1: Ready!"

    def operation_n(self) -> str:
        return "Subsystem1: Go!"

class Subsystem2:
    """
    Some facades can work with multiple subsystems at the same time.
    """

    def operation1(self) -> str:
        return "Subsystem2: Get ready!"

    # ...

    def operation_z(self) -> str:
        return "Subsystem2: Fire!"

class Facade:

    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2):
        self._subsystem1 = subsystem1
        self._subsystem2 = subsystem2

    def operation(self) -> str:
        """
        The Facade's methods are convenient shortcuts to the sophisticated
        functionality of the subsystems. However, clients get only to a fraction
        of a subsystem's capabilities.
        """

        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "success!"


if __name__ == "__main__":
    print(Facade(Subsystem1(), Subsystem2()).operation())

