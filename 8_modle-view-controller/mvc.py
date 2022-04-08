# Model
class Database(object):
    def __init__(self):
        self._malwares_info = []

    def get_info(self):
        return self._malwares_info

    def add_info(self, malware_info):
        self._malwares_info.append(malware_info)
        return True


# View
class Page(object):
    def list_malware_info(self, malwares_info):
        for malware_info in malwares_info:
            print("="*30)
            print("file name : %s" % malware_info['filename'])
            print("tag : %s" % malware_info['tag'])
            print("="*30)

    def show_success_add_info(self, is_success):
        if is_success:
            print("add info : Success")
        else:
            print("add info : Failed")


# Controller
class Controller(object):
    def __init__(self):
        self.database = Database()
        self.page = Page()

    def get_malware_info(self):
        malwares_info = self.database.get_info()
        return(self.page.list_malware_info(malwares_info))

    def add_malware_info(self, malware_info):
        is_success = self.database.add_info(malware_info)
        return(self.page.show_success_add_info(is_success))


controller = Controller()
controller.add_malware_info({"filename": "installer.exe", "tag": "ransomware"})
controller.add_malware_info({"filename": "testing.exe", "tag": "infostealer"})
controller.get_malware_info()
