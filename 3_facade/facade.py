# SubSystem 1
class Linux(object):
    def remove_some_data():
        pass


# SubSystem 2
class Unix(object):
    def remove_some_data():
        pass


# Facade
class Manager(object):
    def remove_data(self):
        self.linux = Linux()
        self.linux.remove_some_data()

        self.unix = Unix()
        self.unix.remove_some_data()


# Client
class Developer(object):
    def clear_data(self):
        manager = Manager()
        manager.remove_data()
