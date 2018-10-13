from flask import render_template
import connexion

# Create the app instance
app = connexion.App(__name__, specification_dir='./')

# Configure endpoints
app.add_api('swagger.yml')

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
    app.run(host='0.0.0.0', port=5000, debug=True)

