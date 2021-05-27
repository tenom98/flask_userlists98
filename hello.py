from flask import Flask , render_template
app = Flask(__name__)
#app.debug = True

@app.route('/', methods=['GET', 'POST']) 
def hello_world():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')

if __name__ == '__main__':
    app.run(port=5000)
