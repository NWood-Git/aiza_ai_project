
class Cohort:
    instances = {}

    def __init__(self, cohort_id, cohort_name):
        self.cohort_id = cohort_id
        self.students = {}
        self.cohort_name = cohort_name
        self.__class__.instances[self.cohort_id] = self

    @property
    def cohort_id(self):
        return self._cohort_id

    @cohort_id.setter
    def cohort_id(self, cohort_id):
        self._cohort_id = cohort_id
    
    @property
    def students(self):
        return self._students 

    @students.setter
    def students(self, students):
        self._students = students

    @property
    def cohort_name(self):
        return self._cohort_name

    @cohort_name.setter
    def cohort_name(self, cohort_name):
        self._cohort_name = cohort_name

