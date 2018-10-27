
from flask import (
    Flask,
    render_template
)

# create basic flask application
app = Flask(__name__, template_folder = "templates")

#create URL route in our application for home "/"
@app.route('/')
def home():
    """
    this function just responds to the browser URL
    localhost:5000

    :return: the rendered templatye 'home.html
    """
    return render_template('home.html')


# If we'r running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)




