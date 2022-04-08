from abc import ABCMeta, abstractmethod


# AbstractClass
class System(metaclass=ABCMeta):
    @abstractmethod
    def get_mac_address(self):
        pass

    @abstractmethod
    def get_ip_address(self):
        pass

    def run(self):
        info = []
        mac_address = self.get_mac_address()
        ip_address = self.get_ip_address()
        info.append(mac_address)
        info.append(ip_address)
        return info


# ConcreteClass
class Window(System):
    def get_mac_address(self):
        return "11:22:33:44:55:66"

    def get_ip_address(self):
        return "98.76.54.32"


# ConcreteClass
class Linux(System):
    def get_mac_address(self):
        return "aa:bb:cc:dd:ee:ff"

    def get_ip_address(self):
        return "12.34.56.78"


# Client
class Manager:
    def collect_info(self):
        self.window = Window()
        self.linux = Linux()
        print(self.window.run())
        print(self.linux.run())


manager = Manager()
manager.collect_info()
