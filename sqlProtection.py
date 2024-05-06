import re
from flask import abort

def sql_injection_protection(sql_query):
    # identifying the injection string that can be used to bypass password entry in user form
    injection_string = '; -- '
    # if the injection string is found in the query, abort the call to the db
    if sql_query.__contains__(injection_string):
        abort(400, 'Potential SQL Injection')
    # otherwise, return the query to be sent to the db
    else:
        return sql_query


def check_query_parameterized(sql_query):
    # defining the regular expression patter to match a parameterized SQL query
    input_parameter_pattern = r'\b(?:\?|%s)\b'

    # find the count of present parameter placeholders for the supplied sql query
    query_parameters = len(re.findall(
        input_parameter_pattern, sql_query, re.IGNORECASE))

    # variable to store boolean value if query is parameterized or not
    is_parameterized = False
    # return a boolean as to whether the query is parameterized or not
    if query_parameters == 0:
        is_parameterized = False
    else:
        is_parameterized = True

    # return the sql query if it is parameterized; abort otherwise
    if is_parameterized == True:
        return sql_query
    else:
        abort(400, 'Unparameterized SQL Query')
    