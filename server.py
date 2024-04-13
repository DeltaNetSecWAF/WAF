from flask import Flask, request, render_template, abort
import re

app = Flask(__name__)

ALLOWED_TAGS = ['<p>', '<br>', '<strong>', '<em>', '<ul>', '<li>', '<ol>']


def sanitize_input(input_string):
    # Implement your input sanitization logic here
    # This is a basic example; you may want to use a library like Bleach for more comprehensive sanitization
    sanitized_string = ''.join(
        c for c in input_string if c.isalnum() or c.isspace() or c in ['-', '_'])
    return sanitized_string


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


@app.route('/submit', methods=['POST'])
def submit_form():
    print("got the request!")
    user_input = request.form.get('input')
    print(user_input)

    sanitized_input = sanitize_input(user_input)

    # Check if the sanitized input matches the original input
    if sanitized_input != user_input:
        # Log or take action against potential XSS attack
        abort(400, 'Potential XSS attack detected')

    # Process the sanitized input
    # Your application logic goes here

    return render_template('success.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
