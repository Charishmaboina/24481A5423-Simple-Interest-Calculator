
from flask import Flask, render_template, request, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/greet/<uname>')
def greet(uname):
    return f"Hello, {uname}!"

@app.route('/delete/<int:roll>')
def delete_user(roll):
    return f"Deleting record with roll number: {roll}"
''''''

@app.route('/calculate', methods=['GET', 'POST'])
def Si():
    if request.method == 'POST':
        principal = float(request.form['p'])
        rate = float(request.form['r'])
        time = float(request.form['t'])
        simple_interest = (principal * rate * time) / 100
        total_amount = principal + simple_interest
        return render_template('index.html', result=simple_interest, total_amount=total_amount, principal=principal, rate=rate, time=time)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=2500)
s