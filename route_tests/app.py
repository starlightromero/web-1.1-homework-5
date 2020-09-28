"""Import flask and unittest."""
from flask import Flask, request
from unit_tests.string_functions import reverse

app = Flask(__name__)


@app.route("/")
def index():
    """Home page."""
    return "Hello, World!"


@app.route("/color_form")
def show_color_form():
    """Color form page."""
    return """
    <form action="/color_results" method="GET">
        <label>
            What's your favorite color?
            <input type="text" name="color">
        </label>
        <input type="submit" name="Submit!">
    </form>
    """


@app.route("/color_results")
def process_color_results():
    """Color form results page."""
    users_favorite_color = request.args.get("color")
    if not users_favorite_color:
        return "I love all colors!"
    return f"Wow, {users_favorite_color} is my favorite color, too!"


@app.route("/froyo")
def choose_froyo():
    """Show a form to collect the user's Fro-Yo order."""
    return """
    <form action="/froyo_results" method="GET">
        What is your favorite Fro-Yo flavor? <br/>
        <input type="text" name="flavor"><br/><br/>
        What toppings do you want?
        <input type="text" name="toppings"><br/>
        <input type="submit" value="Submit!">
    </form>
    """


@app.route("/froyo_results")
def show_froyo_results():
    """Show froyo order results to user."""
    users_froyo_flavor = request.args.get("flavor")
    toppings = request.args.get("toppings")
    if not users_froyo_flavor and not toppings:
        return "We didn't receive your order."
    if not users_froyo_flavor:
        return f"You ordered {toppings}! Come back next time to try Fro-Yo."
    if not toppings:
        return f"You ordered {users_froyo_flavor} flavored Fro-Yo!"
    return f"You ordered {users_froyo_flavor} flavored Fro-Yo with toppings {toppings}!"


@app.route("/reverse_message")
def reverse_message_form():
    """Show form for user to input message to be reversed."""
    return """
    <form action="/message_results" method="POST">
        What's your message?
        <input type="text" name="message">
        <input type="submit" value="Submit!">
    </form>
    """


@app.route("/message_results", methods=["POST"])
def message_results():
    """Show message result as reversed string."""
    message = request.form.get("message")
    if not message:
        return "We didn't receive a message."
    reversed_message = reverse(message)
    return f"Here's your reversed message: {reversed_message}"


@app.route("/calculator")
def calculator():
    """Show calculator form to user."""
    return """
    <form action="/calculator_results" method="GET">
        Please enter 2 numbers and select an operator.<br/><br/>
        <input type="number" name="operand1">
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="number" name="operand2">
        <input type="submit" value="Submit!">
    </form>
    """


@app.route("/calculator_results")
def calculator_results():
    """Show calculator results from form."""
    try:
        operand1 = int(request.args.get("operand1"))
        operand2 = int(request.args.get("operand2"))
        operation = request.args.get("operation")
        if operation == "add":
            result = operand1 + operand2
        elif operation == "subtract":
            result = operand1 - operand2
        elif operation == "multiply":
            result = operand1 * operand2
        elif operation == "divide":
            result = operand1 / operand2
        return f"""
You chose to {operation} {operand1} and {operand2}.
Your result is: {result}
"""
    except ValueError:
        return "Please enter a valid number and operation."


if __name__ == "__main__":
    app.run(debug=True)
