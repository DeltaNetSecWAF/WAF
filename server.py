from flask import Flask, request, render_template, abort
from rate_limiter import RateLimiter
from xssScaner import Scan
from sqlProtection import sql_injection_protection

app = Flask(__name__)
rateLimiter = RateLimiter(5, 1)



def sanitize_input(input_string):
    # Implement your input sanitization logic here
    # This is a basic example; you may want to use a library like Bleach for more comprehensive sanitization
    sanitized_string = ''.join(
        c for c in input_string if c.isalnum() or c.isspace() or c in ['-', '_'])
    return sanitized_string



@app.route('/submit', methods=['POST'])
def submit_form():
    print("got the request!")
    ip = request.remote_addr

    #DDoS protection 
    rateLimiter.addRequest(ip)
    if (rateLimiter.hasExceededLimit(ip)):
        print(f"rate limit hit by ${ip}")
        return "Rate limit hit"
    
    #XSS protection
    user_input = request.form.get('input')
    if Scan(user_input):
        abort(400, 'Possible XSS Attack Detected')
    
    #sql injection protection
    sql_injection_protection(user_input)

    return "Success"


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
