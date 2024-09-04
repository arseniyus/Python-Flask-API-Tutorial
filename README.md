Hi! Welcome to my Python Flask API Tutorial Workshop.

## Why Python? 🐍

Python is a very popular and common programming language. It is on par in popularity with JavaScript. Python is used in everything from web/software development, automation, machine learning, data analysis, and data visualization.

Why not just stick with JavaScript, as it does a lot of that just as well? It is good to be tech-agnostic. It encourages flexibility of thinking, confidence, and fosters problem-solving. Also, broadening your toolset as a bootcamper increases your chances of being hired. The more you learn, the more you earn!

## Why Flask? 🧪

Flask is a Python web framework that allows you to build lightweight (loads quickly) web apps very quickly and easily.
It is known as a microframework, as it keeps the crux of the app simple and scalable.

- However, it doesn't include things like ORM (Object Relational Manager) or form validation by itself.

- But! It is extendable, meaning you can extend its functionality through various extensions. For example, you can choose to add validation.

- Flask is built on top of the Werkzeug WSGI toolkit, which handles request/response objects and utility functions.
  Jinja2 is Flask's template engine for rendering dynamic web pages. It essentially acts like Python's "React." It also allows you to pass Python variables into HTML templates, similar to JSX.

P.S. Don't worry about remembering all of that. This is just for your understanding and awareness.

- Easy to use: Flask has a very small learning curve, making it perfect for beginners.

- Local Development: You can "local host" with it. 😁

### Core Concepts

Never coded in Python? Don't worry. It is eerily similar to JavaScript.
For example: A basic multiplication function in JS would look like:

`function multiply(a, b) {`
`return a \* b;`
`}`
`const result = multiply(2, 4);`
`console.log(result);`

And in Python:
`def multiply(a, b):`
`return a \* b`
`result = multiply(2, 4)`
`print(result)`

The difference? Just the syntax (the grammar of a programming language).
Let's look at some key differences:

- No variables (let, const, var) just x = 10 in Python (let x = 10 in JS).

- def === function

- No curly braces { } Instead, Python uses indentation to scope out blocks (multiple lines) of code. For example: A lot of indentation without appropriate indentation, the code won't work.

- : (colons) instead of ; (semi-colons) Unlike JS, it is needed to make the function run, though statements end on a new line.

- Python likes_snake_case as opposed to camelCase in JS. Ssssssssssssss 🐍 remember_always_use_underscores_and_lowercase

- A lot of the JS methods (a pre-defined mini-function within a programming language, e.g., toString(), .length, toUpperCase, console.log()) with which you may already be familiar also exist in some capacity in Python. For example, all of the above exist. It might be worded differently, like print === console.log. But that is where Google and documentation are helpful.

Here is some Python documentation to get you started: https://pythonbasics.org/

### Ticket 1) ### The Setup

# a) Install Python

- Option 1: Go to the 'Microsoft Store,' search for Python, and install any 3.x version. The latest stable version is 3.12.5 (I use 3.13).

- Option 2: Go to https://www.python.org/downloads/ - Install Python on your system.

On install, make sure you check both:
'Use admin privileges when installing py.exe' and
'Add python.exe to PATH'

Why? This will save you a lot of time in the future when using any command prompt or terminal without needing to specify the full path.

- Then, in VSC, click on 'Extensions,' search for 'Python,' and click 'Install.'

- To verify that Python installed successfully, type `'python --version'` in the terminal.

For any issues, go to: https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites and troubleshoot.

# b) Create a virtual environment

This is a common best practice among Python developers. It keeps the packages you install here isolated from all of your other environments, and therefore projects, just in case things go wrong.

- Press 'Ctrl+Shift+P'
- Type: 'Python: Create Environment'
- Select 'Venv.'
- Select the version of Python you just installed.

It will then install, and a .venv folder will appear at the root of your directory.

# c) Create a .gitignore file

- Just type '.gitignore' when creating a file.
- In the .gitignore file, type in 'venv/'. This will make sure your venv file doesn't get pushed into the repository when you git add.
- If, upon git adding, git still tracks the .venv folder, don't worry. Just type this in the terminal: `'git rm -r --cached .venv/'`

This will remove the changes from the commit.

# d) Create a file called app.py

# e) Install Packages

We need to install 3 things:

1. Flask by typing: 'pip install Flask'
2. request: 'pip install request'
3. jsonify: 'pip install jsonify'

## Ticket 2) Is this thing on?

Write some code to define your API endpoints and logic.

In your file, write a simple message along the lines of: "Hello World!"

`@app.route("/", methods=["GET"])`
`def test():`
`if request.method == "GET":`
`return jsonify({"response": "Hello There!"})`

Does this look familiar? It should! 😄
This is the twin brother:

`app.get('/', (req, res) => {`
`res.json({ response: "Hello There!" });`
`})`

Let's do a quick breakdown of the syntax of the original Python function:

- app.route("any string", methods=["GET"])
- def test(): (A function with any name) If we are making a GET request: - Return a JSON object ({"key": "value"}).

Normally in JavaScript, you will need to define the logic of the get request function in a separate place.
But Python lets you define both the endpoint and the logic all in one place! Neat, right? 😍

Test it by typing `'python app.py'` in the terminal.
Expected outcome: Your custom message should appear in localhost upon clicking on the hyperlink in the terminal.

## Ticket 3)

Run the server and make the first API call using a tool like Postman or curl.

## Ticket 4)

a) Implement different HTTP methods like GET, POST, PUT, and DELETE for your API.

b) Test all of the above endpoints using a tool like Postman.
