from flask import Flask, render_template, request
from data import connect_db


app = Flask(__name__)


@app.route('/user/<int:user_id>')
def user_profile(user_id):
    database, cursor = connect_db()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    for user in users:
        if user[0] == user_id:
            return f"User Profile: {user[1]}"
        
    return "User not found!"

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    age = request.form['age']
    database, cursor = connect_db()
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    database.commit()
    return "User seved"



@app.route('/add_user', methods=['GET'])
def add_user_form():
    return render_template('add_user.html')



if __name__ == "__main__":
    app.run(debug=True)
