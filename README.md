# Python-Flask-API-Tutorial

Hi! Welcome to my Python Flask API Tutorial Workshop

### Why

- Why Python? 🐍

Python is a very popular and common programming language. It is on par in popularity with JavaScript.
Python is used in everything from web/software development, automation, machine learning, data analysis and data visualisation.

Why not just stick with JavaScript, it does a lot of that just as well?
It is good to be tech agnostic. It encourages flexibility of thinking, confidence, and fosters problem-solving.
Also, broadening your toolset as a bootcamper increases your chances of being hired. The more you learn the more you earn!

- Why Flask? 🧪
  Flask is a Python web framework that allows yout to buiuld lightweight (loads quickly) web apps very quickly and easily.

* It is known as a microframework, as it keeps the crux of the app simple and scaleable.

- But it doesn't include things like ORM (Object Relational Manager) or form validation, by itself.

* It is however extendable. Meaning, you can extend its functionality through various extensiuons. E.g you can choose to add validation.
* Flask is built on top of the Werkzeug WSGI toolkit, which handles req, res objects and utility functions.
* Jinja2 is Flasks' template enginne for rendering dynamic web pages. It essentially acts like Python's "React". It also allows you to pass Python variabls into HTML templates. (Similar to JSX).

P.S. Don't worry about remembering all of that. This is just for your understanding and awareness.

- Easy to use. Flask has a very small learning curve. Perfect for beginners.
- Local Development: you can "local host" with it. 😁

### Core Concepts

Never coded in Python? Don't worry. It is eerily similar to JavaScript.

For example:
A basic multiplication function in JS would look like:

`function multiply(a, b)` {
`return = a \* b;`
}
`const result = multiply(2, 4)`
`console.log(result);`

And in Python:
`def multiply(a, b):`
`return a \* b`

`result = multiply(2, 4)`
`print(result)`

The difference? Just the syntax (The grammar of a programming language).

Let's look at some key differences:

- No variables (let, const, var)
  just `x = 10` in Python (`let x = 10 in JS`)
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
  Ssssssssssssss 🐍
  remember_alwasy_use_underscores_and_lowercase

A lot of the JS methods (a pre-defined mini function within a programing language e.g. `toString(), .length, toUpperCase, console.log())` - with which you may already be familiar with also exist in some capacity in Python.
E.g. All of the above exist. It might be worded differently like print === console.log.
But that is where google and documentation is helpful.

Here is some Python documentation to get you started:
https://pythonbasics.org/

- Install Flask and set up a virtual environment for your project.
- Create a file app.py.

### Ticket 1) The Set Up

a) Install Python.

- Option 1) Go to 'microsoft store' search for Python install any 3x version. The latest stable version is 3.12.5 (I use 3.13)
- Option 2) Go to https://www.python.org/downloads/ - Install Python on your system

- On Install make sure you check both:
  'Use admin privileges when installing py.exe' AND
  'Add python.exe to PATH'

  Why?
  This will save you a lot of time in the future when using any command prompt or terminal without needing to specify the full path.

- Then, in VSC click on 'extensions', search for 'Python', and click 'Install'

- To verify that python installed successfully type in `'python --version'` in the terminal.

- For any issues: go to: https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites and troubleshoot.

b) Create a virtual environment
This is a comon best practice amongst Python devs. It keeps the packages you install here isolated from all of your other environments, and therefore porjects, just in case things go wrong.

- Press `'Ctrl+Shift+p'`
- Type: 'Python: Create Environment'
- Select 'Venv'
- Select the version of Python you just installed
- It will then install and a .venv folder will appear at the root of your directory.

c) Create a gitignore file

- Just type when creating a file '.gitignore'
- In the git ignore file type in 'venv/'
  This will make sure your venv file doesn't get pushed into the repository when you git add.

IF upon git adding, git still tracks the .venv folder, don't worry. Just type this in the terminal:
`'git rm -r --cached .venv/'`

This will remove the changes from the commit.

d) Create a file called app.py

e) Install Packages.
We need to Install 3 things:

- Flask by typing: 'pip install Flask'
- request: 'pip install request'
- jsonify: 'pip install jsonify'

### Ticket 2) Is this thing on?

Write some code to define your API endpoints and logic.

- In your file write a simple message along the lines of:
  "Hello World!"

`@app.route("/", methods=["GET"])`
`def test():`
`if request.method == "GET":`
`return jsonify({"response": "Hello There!"})`

Does this look familiar?
It should! 😄

This is the twin brother
`app.get('/', (req, res) => {`
`res.json({ response: "Hello There!" });`
`})`

Let's do a quick breakdown of the syntax of the original Python function:

- app.with_this_route("any string", methods=["GET request])
- def test(): (A function with any name)
  if we are making a GET request:
  return a json object({"key": "value"})

Normally in JavaScript you will need to define the logic of the get request funcition in a seperate place.
But Python let's you define both the endpoint and the logic all in one place! Neat right? 😍

- Test it by typing 'python app.py' in the terminal

Expected outcome: your custom message should appear in local host, upon clicking on the hyperlink in the terminal.

### Ticket 3) Complete as many CRUD Operations as you can

a) Make a basic GET all resource request
Let's apply the knowledge gained from the above syntax and apply it.

In the Repository you will note that the GET request has already been completed for you.
`@app.route("/games", methods=["GET"])`
`def get_games():`
`return jsonify(Games)`

Are you seeig a pattern here?

- Run the server (python app.py) and make the first API call using a tool like Postman.

b) Make a basic POST request

c) Make a basic GET by ID request

d) Make a basic DELETE request

e) Make a basic PUT request

f) Make a basic PATCH request
