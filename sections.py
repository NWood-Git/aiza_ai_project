import sqlite3 as sql
from sqlite3 import Error
import section_names

def give_sect_nums():
    global_var_lst = dir(section_names)
    module_section_list = []
    for item in global_var_lst:
        if item[0:6] == "MODULE":
            module_section_list.append(int(str(item[7]) + str(item[17])))
    return module_section_list

class Section:

    instances = {}

    def __init__(self, section_id, grades):
        self.section_id = section_id
        self.__class__.instances[self.section_id] = self
        self.grades = grades

    @property
    def section_id(self):
        return self._section_id

    @section_id.setter
    def section_id(self, section_id):
        self._section_id = section_id

    @property
    def grades(self):
        return self._grades
    
    @grades.setter
    def grades(self, grades):
        self._grades = grades


  # def get_grades(self, grades):
    #     self.grades = grades

    # @classmethod
    # def create_section_ids(cls):
    #     '''Creates Section instance for every section_id'''
    #     section_lst = give_sect_nums()
    #     # print(section_lst)
    #     for section in section_lst:
    #         sections = Section(section_id = section)
            
    
# Section.create_section_ids()
# print(Section.instances)