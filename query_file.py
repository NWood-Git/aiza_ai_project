import sqlite3
from section_names import SECTION_NAMES

dbpath = 'mydb.db'

# These queries will be used to get data from the db into the query engine

def give_sect_nums():
    '''Returns a list strings for all the Module / Section variable names'''
    module_section_list = []
    for key in SECTION_NAMES:
        if key[0:6] == "MODULE":
            module_section_list.append(str(key[7]) + str(key[17]))
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

def select_all_stud_table_by_cohort(cohort_id):
    with sqlite3.connect(dbpath) as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()
        SQL = f"Select * FROM students where cohort_id = {cohort_id};"
        cur.execute(SQL)
        rows = cur.fetchall()
        return rows

def grade_getter_for_section(num_section):
    '''This function takes in a 2-digit string for the section name and'''
    '''outputs a dict of stud_id : section_grade (sum of points on exercises)'''
    sect_name = "MODULE_"+ num_section[0] + "_SECTION_" + num_section[1]
    sect_name = SECTION_NAMES[sect_name]
    all_grades_dict_list = select_all_from_table(sect_name)
    # print(all_grades_dict_list)
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
        # print(total_points)
        result_dict[stud_id] = total_points
    return result_dict
    


if __name__ == '__main__':
    # print(select_all_from_table(SECTION_NAMES['MODULE_1_SECTION_1'])) #'grades_intro_to_cs'
    # print(select_all_from_table(SECTION_NAMES['MODULE_1_SECTION_2'])) #'grades_IDEs'
    # print(select_all_by_1_stud_id(SECTION_NAMES['MODULE_1_SECTION_2'],2)) #grades_IDE
    # print(select_all_stud_table_by_cohort(1))
    # # print(grade_getter_for_section('11'))
    # print(give_sect_nums())
    pass

#the below returns a list of dicts

# def select_all_from_table(tablename):
#     with sqlite3.connect(dbpath) as conn:
#         conn.row_factory = sqlite3.Row
#         cur = conn.cursor()
#         SQL = f"Select * FROM {tablename};"
#         cur.execute(SQL)
#         rows = cur.fetchall()
#         result = [list(row) for row in rows]
#         return result

# def select_all_by_stud_id(tablename, stud_id):
#     with sqlite3.connect(dbpath) as conn:
#         conn.row_factory = sqlite3.Row
#         cur = conn.cursor()
#         SQL = f"Select * FROM {tablename} where stud_id = {stud_id};"
#         cur.execute(SQL)
#         rows = cur.fetchall()
#         result = [list(row) for row in rows]
#         return result

# def select_all_stud_by_cohort(cohort_id):
#     with sqlite3.connect(dbpath) as conn:
#         conn.row_factory = sqlite3.Row
#         cur = conn.cursor()
#         SQL = f"Select * FROM students where cohort_id = {cohort_id};"
#         cur.execute(SQL)
#         rows = cur.fetchall()
#         result = [list(row) for row in rows]
#         return result
