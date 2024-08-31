# Python-Flask-API-Tutorial

Hi! Welcome to my Python Flask API Tutorial Workshop

### Why

- Why Python?

Python is a very popular and common programming language. It is on par in popularity with JavaScript.
Python is used in everything from web/software development, automation, machine learning, data analysis and data visualisation.

Why not just stick with JavaScript, it does a lot of that just as well?
It is good to be tech agnostic. It encourages flexibility of thinking, confidence, and fosters problem-solving.
Also, broadening your toolset as a bootcamper increases your chances of being hired. The more you learn the more you earn!

- Why Flask?
  Flask is a Python web framework that allows yout to buiuld lightweight (loads quickly) web apps very quickly and easily.

* It is known as a microframework, as it keeps the crux of the app simple and scaleable.

- But it doesn't include things like ORM (Object Relational Manager) or form validation, by itself.

* It is however extendable. Meaning, you can extend its functionality through various extensiuons. E.g you can choose to add validation.
* Flask is built on top of the Werkzeug WSGI toolkit, which handles req, res objects and utility functions.
* Jinja2 is Flasks' template enginne for rendering dynamic web pages. It essentially acts like Python's "React". It also allows you to pass Python variabls into HTML templates. (Similar to JSX).

P.S. Don't worry about remembering all of that. This is just for your understanding and awareness.

- Easy to use. Flask has a very small learning curve. Perfect for beginners.
- Local Development: you can "local host" with it. :)

### What

Ticket 1) The Set up.

Never coded in Python? Don't worry. It is eerily similar to JavaScript.

For example:
A basic multiplication function in JS would look like:

function multiply(a, b) {
return = a \* b;
}
const result = multiply(2, 4)
console.log(result);

And in Python:
def multiply(a, b):
return a \* b

result = multiply(2, 4)
print(result)

The difference? Just the syntax (The grammar of a programming language).

Let's look at some key differences:

- No variables (let, const, var)
  just x = 10 in Python (let x = 10 in JS)
- Def === function
- No curlies ( {} )
  instead Python uses indentation to scope out blocks (multiple lines) of code.
  e.g.
  A lot of indentantion
  without approprate indentation
  the code
  won't work.
- : (colons) instead of ; (semi-colons)
  and unlike JS it is needed to make the function run. Though statements end on new line.
- python_likes_snake_case as oposed to camelCase in Js.
  Ssssssssssssss
  remember_alwasy_use_underscores_and_lowercase

A lot of the JS methods (a pre-defined mini function within a programing language e.g. toString(), .length, toUpperCase, console.log()) - with which you may already be familiar with also exist in some capacity in Python.
E.g. All of the above exist. It might be worded differently like print === console.log.
But that is where google and documentation is helpful.

Here is some Python documentation to get you started:
https://pythonbasics.org/

- Install Flask and set up a virtual environment for your project.
- Create a file app.py.

Ticket 2)
a) Install Python.
- In VSC click on 'extensions', search for 'Python', and click 'Install' 
-  Create a file called app.py
- Type 'PIP install' in the terminal hit enter. 
- The terminal will prompt you to create a virtual environment.
- (Optional alternative) Go to https://www.python.org/downloads/
- On Install make sure you check both:
    'Use admin privileges when installing py.exe' AND
    'Add python.exe to PATH'
This will save you a lot of time in the future when ausing any command prompt or terminal without needing to specify the full path.

- write some code to define your API endpoints and logic.

Ticket 3) Run the server and make the first API call using a tool like Postman or curl.

Ticket 4) Implement different HTTP methods like GET, POST, PUT, and DELETE for your API.

Ticket 5) Create a class to represent your data model and set up a SQLite database connection.
