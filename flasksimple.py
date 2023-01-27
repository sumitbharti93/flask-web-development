from flask import Flask , render_template
app = Flask(__name__)


posts = [
    {
        'author' : 'Sumit Bharti',
        'title' : 'web development',
        'content' : 'First post',
        'date_posted' : '26 Jan 2023'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title ="about")


if __name__ == "__main__":
    app.run(debug = True)