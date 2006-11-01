from flask import Blueprint, render_template

pages = Blueprint(
    'pages',
    __name__,
    template_folder='templates')
    

@pages.route('/')
def index():
    return render_template('index.html')


@pages.route('/about')
def about():
    return render_template("about.html") 


@pages.route('/contact')
def contact():
    return render_template("contact.html") 


@pages.route('/experience')
def experience():
    return render_template("experience.html")


@pages.route('/groups')
def groups():
    return render_template("groups.html") 


@pages.route('/howicanhelp')
def howicanhelp():
    return render_template("howcanihelp.html") 


@pages.route('/resources')
def resources():
    return render_template("resources.html") 


@pages.route('/testimonials')
def testimonials():
    return render_template("testimonials.html") 


@pages.route('/pretendfriends')
def pretendfriends():
    return render_template("pretendfriends.html") 