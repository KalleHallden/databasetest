from flask import Flask, request

app = Flask(__name__)

@app.route("/")

def hello():
    return "Hello world"

@app.route("/name/<name>")

def get_book_name(name):
    return "name : {}".format(name)

@app.route("/details")
def get_bok_details():
    author = request.args.get('author')
    published = request.args.get('pubished')
    return "Author: {}, Published: {}".format(author,published)


@app.route("/users")
def get_all_users():
    users = ['Kalle', 'Pelle', 'Lelle', 'Kjelle']
    listOfUsers = ""
    for user in users:
        listOfUsers += "\n{}".format(user)
    return listOfUsers

@app.route("/<name>")
def get_user(name):
    return "This is your profile {}".format(name)

if __name__ == '__main__':
    app.run