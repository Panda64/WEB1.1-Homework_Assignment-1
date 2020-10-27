# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

from flask import Flask

app = Flask(__name__)


@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def dessert(users_dessert):
    return f"How did you know I liked {users_dessert}?"

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    return f"Today I will {adjective} at {noun}."

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    if number1.isdigit() == True and number2.isdigit() == True:
        result = int(number1) * int(number2)
        return f"{number1} times {number2} is {result}"
    else:
        return "Invalid Inputs. Please try again by entering 2 numbers!"

if __name__ == '__main__':
    app.run(debug=True)
