import sqlite3 as sql
from sqlite3 import Error
import section_names

def give_sect_nums():
    '''Returns a list strings for all the Module / Section variable names'''
    module_section_list = []
    sec.__dict__
    for key in SECTION_NAMES:
        if key[0:6] == "MODULE":
            module_section_list.append(str(key[7]) + str(key[17]))
    return module_section_list


class Section:

    instances = []

    def __init__(self, section_id):
        self.section_id = section_id
        self.grades = {}
        self.__class__.instances.append(self)

    def get_grades(self, grades):
        self.grades = grades
    
    
    @classmethod
    def printInstances(cls):
        for instance in cls.instances:
            print(instance)

class Sections:
    def __init__(self, sections):
        self.sections = {}
        

    def create_section_ids():
        section_lst = give_sect_nums()
        # print(section_lst)
        for i in section_lst:
            section = Section(section_id = i)
            # print(index)
        # return sections
Sections.create_section_ids()

print(Section.printInstances())

class Module:
    def __init__(self, module_id):
        self.module_id = module_id
        self.sections = {}
    
    def get_sections(self, sections):
        pass