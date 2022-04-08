from abc import ABCMeta, abstractmethod


# Command
class Button(metaclass=ABCMeta):
    @abstractmethod
    def press(self):
        pass


# ConcreteCommand
class OnButton(Button):
    def __init__(self, receiver):
        self.receiver = receiver

    def press(self):
        self.receiver.on()


# ConcreteCommand
class OffButton(Button):
    def __init__(self, receiver):
        self.receiver = receiver

    def press(self):
        self.receiver.off()


# Receiver
class Television:
    def on(self):
        print("TV On")

    def off(self):
        print("TV Off")


# Invoker
class RemoteControl:
    def __init__(self, on_button, off_button):
        self._on_button = on_button
        self._off_button = off_button

    def on(self):
        self._on_button.press()

    def off(self):
        self._off_button.press()


# Client
television = Television()
on_button = OnButton(television)
off_button = OffButton(television)

remote = RemoteControl(on_button, off_button)
remote.on()
remote.off()
