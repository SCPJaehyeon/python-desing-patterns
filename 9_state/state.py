from abc import abstractmethod, ABCMeta


# State
class Processing(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass


# ConcreteState
class StartProcessing(Processing):
    def run(self):
        print("start processing")


# ConcreteState
class StopProcessing(Processing):
    def run(self):
        print("stop processing")


# Context
class Analyzer(Processing):
    def __init__(self):
        self.state = None

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def run(self):
        self.state.run()


context = Analyzer()
start_state = StartProcessing()
stop_state = StopProcessing()

context.set_state(start_state)
context.run()

context.set_state(stop_state)
context.run()
