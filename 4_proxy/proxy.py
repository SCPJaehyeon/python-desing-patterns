from abc import ABCMeta, abstractmethod


# Subject
class Image(metaclass=ABCMeta):
    @abstractmethod
    def print_image(self):
        pass


# RealSubject
class RealImage(Image):
    def print_image(self):
        print("Real Image.")


# Proxy
class ProxyImage(Image):
    def __init__(self):
        self.origin = RealImage()

    def print_image(self):
        print("Proxy Image.")
        self.origin.print_image()


# Client
class HomePage:
    def __init__(self):
        self.proxy = ProxyImage()

    def show_gallery(self):
        self.proxy.print_image()
