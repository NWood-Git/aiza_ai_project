class Module:

    instances = {}

    def __init__(self, module_id, all_sections):
        self.module_id = module_id
        self.sections = {}
        self.__class__.instances[self.module_id] = self
        for section in all_sections:
            if int(str(section)[0]) == module_id:
                self.sections[section] = all_sections[section]

    
    @property
    def mod_id(self):
        return self._module_id

    @mod_id.setter
    def mod_id(self, module_id):
        self._module_id = module_id

    @property
    def sections(self):
        return self._sections

    @sections.setter
    def setter(self, sections):
        self._sections = sections




######################

    # @classmethod
    # def get_mod_ids(cls):
    #     '''Creates Module instances/Module_ids using Section_ids'''
    #     mod_nums = set(map(lambda section: int(str(section)[0]), Section.instances))
    #     for nums in mod_nums:
    #         module = Module(module_id = nums)

    # def get_sections(self):
    #     '''Returns dictionary of section_id:section object for a Module'''
    #     for key in Section.instances:
    #         if int(str(key)[0]) == self.module_id:
    #             print(self.module_id)