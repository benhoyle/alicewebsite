from flask import Blueprint, render_template

pages = Blueprint(
    'pages',
    __name__,
    template_folder='templates')
    

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template("about.html") 


@app.route('/contact')
def contact():
    return render_template("contact.html") 


@app.route('/experience')
def experience():
    return render_template("experience.html")


@app.route('/groups')
def groups():
    return render_template("groups.html") 


@app.route('/howicanhelp')
def howicanhelp():
    return render_template("howcanihelp.html") 


@app.route('/resources')
def resources():
    return render_template("resources.html") 


@app.route('/testimonials')
def testimonials():
    return render_template("testimonials.html") 
    
@app.route('/pretendfriends')
def pretendfriends():
    return render_template("pretendfriends.html") 