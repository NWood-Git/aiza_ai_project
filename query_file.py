import sqlite3
import section_names

dbpath = 'mydb.db'

# These queries will be used to get data from the db into the query engine

def give_sect_nums():
    '''Returns a list of ints for all the Module / Section variable names. 
        Ex: MODULE_1_SECTION_1 == 11'''
    sec_dict = section_names.__dict__
    module_section_list = []
    for key in sec_dict:
        if key[0:6] == "MODULE":
            x = key.split('_')
            if len(x) != 4:
                raise Exception
            module_section_list.append(int(x[1]+x[3]))
    return module_section_list

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d



def select_all_from_table(tablename):
    with sqlite3.connect(dbpath) as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()
        SQL = f"Select * FROM {tablename};"
        cur.execute(SQL)
        rows = cur.fetchall()
        return rows

def select_all_by_1_stud_id(tablename, stud_id):
    '''Returns the dictionary @ index[0] of a list of dictionaries. 
    where key = col name and value = row val'''
    with sqlite3.connect(dbpath) as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()
        SQL = f"Select * FROM {tablename} where stud_id = {stud_id};"
        cur.execute(SQL)
        rows = cur.fetchall()
        return rows[0]

def select_cohort_ids_names():
    with sqlite3.connect(dbpath) as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()
        SQL = "SELECT cohort_id, name FROM cohorts;"
        cur.execute (SQL)
        rows = cur.fetchall()
        # result = [list(row)[0] for row in rows]
        return rows


def select_stud_ids_by_cohort(cohort_id):
    with sqlite3.connect(dbpath) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        SQL = f"Select stud_id FROM students where cohort_id = {cohort_id};"
        cur.execute(SQL)
        rows = cur.fetchall()
        result = [list(row)[0] for row in rows]
        return result

def grade_getter_for_section(num_section):
    '''This function takes in a n-digit string for the section (module is 1 digit and the rest is the section
        and outputs a dict of stud_id : section_grade (sum of points on exercises)'''
    sect_name = "MODULE_"+ str(num_section)[0] + "_SECTION_" + str(num_section)[1:]
    sect_table = section_names.__dict__[sect_name]
    all_grades_dict_list = select_all_from_table(sect_table)
    result_dict = {}
    for item in all_grades_dict_list:
        easy_count = 0
        med_count = 0
        hard_count = 0
        #iterates through 1 student's dict of section grades
        for key in item:
            if key.lower() == 'stud_id':
                stud_id = item.get(key)
            elif key[0].lower() == 'e':
                easy_count += item[key]
            elif key[0].lower() == 'm':
                med_count += item[key]
            elif key[0].lower() == 'h':
                hard_count += item[key]
        total_points = easy_count*1 + med_count*2 + hard_count*3
        result_dict[stud_id] = total_points
    return result_dict
    


if __name__ == '__main__':
    # print(select_all_from_table('students')) #'grades_intro_to_cs'
    # print(select_all_from_table(SECTION_NAMES['MODULE_1_SECTION_1'])) #'grades_intro_to_cs'
    # print(select_all_from_table(SECTION_NAMES['MODULE_1_SECTION_2'])) #'grades_IDEs'
    # print(select_all_by_1_stud_id(SECTION_NAMES['MODULE_1_SECTION_2'],2)) #grades_IDE
    # print(select_all_by_1_stud_id('students', 2))
    # print(select_stud_ids_by_cohort(1))
    # print(grade_getter_for_section('11'))
    # print(give_sect_nums())
    print(select_cohort_ids_names())
    pass


# not needed - returns dict of stud id, cohort id and stud name
# def select_all_stud_by_cohort(cohort_id):
#     with sqlite3.connect(dbpath) as conn:
#         conn.row_factory = dict_factory
#         cur = conn.cursor()
#         SQL = f"Select * FROM students where cohort_id = {cohort_id};"
#         cur.execute(SQL)
#         rows = cur.fetchall()
#         return rows
# print(select_all_stud_by_cohort(1))

#the below returns a list of dicts

# def select_all_stud_by_cohort(cohort_id):
#     with sqlite3.connect(dbpath) as conn:
#         conn.row_factory = sqlite3.Row
#         cur = conn.cursor()
#         SQL = f"Select * FROM students where cohort_id = {cohort_id};"
#         cur.execute(SQL)
#         rows = cur.fetchall()
#         result = [list(row) for row in rows]
#         return result
