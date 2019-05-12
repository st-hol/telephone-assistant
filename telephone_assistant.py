import re


LIMIT_OF_PROPOSED_OPTIONS = 10

from db_handler import create_connection, create_table, select_all_telephones
from utility.utility_functions import parse_result_set

def get_matching_numbers(phones_list, user_input):
    reg_exp = user_input + ".*"
    r = re.compile(reg_exp)

    matched_results = list(filter(r.match, phones_list))
    return matched_results[:LIMIT_OF_PROPOSED_OPTIONS]

def main():
    database = "telephones.db"

    sql_create_phones_table = """ CREATE TABLE IF NOT EXISTS telephones (
                                           id integer PRIMARY KEY,
                                           number text NOT NULL
                                       ); """

    # create a database connection
    conn = create_connection(database)

    if conn is not None:
        # create phones table
        create_table(conn, sql_create_phones_table)
    else:
        print("Error! cannot create the database connection.")

    phones_list = select_all_telephones(conn)

    phones_list = parse_result_set(phones_list)

    while True:
        user_input = input("Input:\n")
        if user_input == "exit":
            break
        print(get_matching_numbers(phones_list, user_input))

if __name__ == '__main__':
    main()




























#
# import re
#
# LENGTH_OF_TELEPHONE_NUMBER = 12
# LIMIT_OF_PROPOSED_OPTIONS = 10
#
# phones = ["380675674432", "380672832500","380983567721"]
# # r = re.compile("380.{9}")
# # newlist = list(filter(r.match, phones))
# # print(newlist)
#
# def make_regex(user_input):
#     length_of_missing_part = LENGTH_OF_TELEPHONE_NUMBER - len(user_input)
#     reg_exp = user_input + ".{" + str(length_of_missing_part) + "}"
#     r = re.compile(reg_exp)
#
#     matched_results = list(filter(r.match, phones))
#     return matched_results[:LIMIT_OF_PROPOSED_OPTIONS]
#
# print(make_regex("3806728"))