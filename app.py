import os

from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route("/", methods=['POST', 'GET'])
def home():
    return render_template('home.html')


@app.route("/about", methods=['POST', 'GET'])
def about():
    return render_template('about.html')


@app.route("/projects", methods=['POST', 'GET'])
def projects():
    return render_template('projects.html')


@app.route("/contact", methods=['POST', 'GET'])
def contact():
    return render_template('contact.html')


@app.route("/backlog", methods=['POST', 'GET'])
def backlog():
    return render_template('backlog.html')


@app.route("/dll", methods=['POST', 'GET'])
def dll():
    return render_template('DLL.html')


@app.route("/hsc", methods=['POST', 'GET'])
def hsc():
    return render_template('HSC.html')


@app.route("/opal", methods=['POST', 'GET'])
def opal():
    return render_template('OPAL.html')


@app.route("/leetcode", methods=['POST', 'GET'])
def leetcode():
    return render_template('leetcode.html')


@app.route("/lc_contains_duplicate", methods=['POST', 'GET'])
def lc_contains_duplicate():
    return render_template('lc_contains_duplicate.html')


@app.route("/lc_valid_anagram", methods=['POST', 'GET'])
def lc_valid_anagram():
    return render_template('lc_valid_anagram.html')


@app.route("/lc_prod_exc_self", methods=['POST', 'GET'])
def lc_prod_exc_self():
    return render_template('lc_prod_exc_self.html')


@app.route("/lc_group_anagrams", methods=['POST', 'GET'])
def lc_group_anagrams():
    return render_template('lc_group_anagrams.html')


if __name__ == '__main__':
    app.run()
