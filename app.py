from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oTv!5ox8LB#A&@cBHpa@onsKU'


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
    # test
    return render_template('OPAL.html')


if __name__ == '__main__':
    app.run()
