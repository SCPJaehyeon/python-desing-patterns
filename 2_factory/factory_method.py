from abc import ABCMeta, abstractmethod


# Section
class Section(metaclass=ABCMeta):
    @abstractmethod
    def print_describe(self):
        pass


# ConcreteSection
class ImageSection(Section):
    def print_describe(self):
        print("image section")


# ConcreteSection
class VideoSection(Section):
    def print_describe(self):
        print("video section")


# ConcreteSection
class TextSection(Section):
    def print_describe(self):
        print("text section")


# Product
class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        pass

    def get_section(self):
        return self.sections

    def add_section(self, section):
        self.sections.append(section)


# ConcreteProduct
class Facegram(Profile):
    def create_profile(self):
        self.add_section(ImageSection())
        self.add_section(VideoSection())


class Instabook(Profile):
    def create_profile(self):
        self.add_section(ImageSection())
        self.add_section(VideoSection())
