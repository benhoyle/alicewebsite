from flask import (
    Blueprint, render_template, make_response, current_app,
    request
    )

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
    return render_template("howicanhelp.html")


@pages.route('/resources')
def resources():
    return render_template("resources.html")


@pages.route('/testimonials')
def testimonials():
    return render_template("testimonials.html")


@pages.route('/pretendfriends')
def pretendfriends():
    return render_template("pretendfriends.html")


@pages.route('/socialmedia')
def socialmedia():
    return render_template("socialmedia.html")


@pages.route('/sitemap.xml', methods=['GET'])
def sitemap():
    pages = []
    for rule in current_app.url_map.iter_rules():
        if "GET" in rule.methods and len(rule.arguments) == 0:
            pages.append(
                        [rule.rule]
                        )
    url_root = request.url_root[:-1]
    sitemap_xml = render_template(
        'sitemap.xml',
        pages=pages,
        url_root=url_root
        )
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"
    return response
