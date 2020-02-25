class Student:

    instances = {}

    def __init__(self, student_id, stud_name, cohort_id):
        self.student_id = student_id
        self.stud_name = stud_name
        self.cohort_id = cohort_id
        self.sections = {} #section_id: students grade in section
        self.__class__.instances[self.student_id] = self

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, student_id):
        self._student_id = student_id

    @property
    def stud_name(self):
        return self._stud_name 

    @stud_name.setter
    def stud_name(self, stud_name):
        self._stud_name = stud_name
        
    @property
    def cohort_id(self):
        return self._cohort_id

    @cohort_id.setter
    def cohort_id(self, cohort_id):
        self._cohort_id = cohort_id

    @property
    def sections(self):
        return self._sections

    # sections: dict(section_id: section_obj)
    # section_obj: dict(student_id: int)
    # When calling this function, we pass in Section.instances to the sections parameter
    @sections.setter
    def sections(self, section_dict):
        self._sections = {}
        for key in section_dict:
            cur_section = section_dict[key] #Section obj
            for stud_id in cur_section:
                if self.student_id == stud_id:
                    self._sections[cur_section.get_id()] = cur_section[self.student_id]
