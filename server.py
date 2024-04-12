from flask import Flask, request, render_template, abort

app = Flask(__name__)

# Example list of allowed HTML tags
ALLOWED_TAGS = ['<p>', '<br>', '<strong>', '<em>', '<ul>', '<li>', '<ol>']

# Function to sanitize input and prevent XSS
def sanitize_input(input_string):
    # Implement your input sanitization logic here
    # This is a basic example; you may want to use a library like Bleach for more comprehensive sanitization
    sanitized_string = ''.join(c for c in input_string if c.isalnum() or c.isspace() or c in ['-', '_'])
    return sanitized_string

# Route for handling user input
@app.route('/submit', methods=['POST'])
def submit_form():
    user_input = request.form.get('user_input')

    # Sanitize user input to prevent XSS
    sanitized_input = sanitize_input(user_input)

    # Check if the sanitized input matches the original input
    if sanitized_input != user_input:
        # Log or take action against potential XSS attack
        abort(400, 'Potential XSS attack detected')

    # Process the sanitized input
    # Your application logic goes here

    return render_template('success.html')

# Sample template for the form
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
