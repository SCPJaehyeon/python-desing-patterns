from abc import ABCMeta, abstractmethod


# Observer
class System(metaclass=ABCMeta):
    @abstractmethod
    def alert(self):
        pass


# Subject
class SystemController:
    def __init__(self):
        self._systems = []

    def add_system(self, system: System):
        self._systems.append(system)

    def alert_all_system(self, *args, **kwargs):
        for system in self._systems:
            system.alert(self, *args, **kwargs)


# ConcreteObserver
class Linux(System):
    def __init__(self, controller: SystemController):
        controller.add_system(self)

    def alert(self, controller, *args):
        print("I'm " + type(self).__name__)
        print("Alert : " + args[0])
        print(controller)


# ConcreteObserver
class Unix(System):
    def __init__(self, controller: SystemController):
        controller.add_system(self)

    def alert(self, controller, *args):
        print("I'm " + type(self).__name__)
        print("Alert : " + args[0])
        print(controller)


controller = SystemController()
linux = Linux(controller)
unix = Unix(controller)
controller.alert_all_system("hello world")
