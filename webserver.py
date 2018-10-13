from flask import (
	Flask,
	render_template
)

# Create the app instance
app = Flask(__name__, template_folder="templates")

# Create an URL route in app for "/"

@app.route('/')
def home():
    """
    This function responds to the browser URL localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

# if we are not a module, run app
if __name__ == '__main__':
    app.run(debug=True)

