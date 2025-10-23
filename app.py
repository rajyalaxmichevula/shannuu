from flask import Flask, render_template, request, redirect, url_for, flash
from flask import Response

app = Flask(__name__)
app.secret_key = "secretkey"

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username', '').strip()
    password = request.form.get('pwd', '').strip()

    if username == "":
        return Response("<script>alert('Username cannot be empty.'); window.location.href='/'</script>")
    elif password == "":
        return Response("<script>alert('Password cannot be empty.'); window.location.href='/'</script>")
    elif len(password) < 6:
        return Response("<script>alert('Password must be at least 6 characters long.'); window.location.href='/'</script>")
    else:
        return render_template('greeting.html', name=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001,debug=True)
