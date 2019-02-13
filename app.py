from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/welcome/<string:student_name>")
def welcome(student_name):
    return render_template('welcome.html', student_name=student_name)

#'/welcome/' This message should display a welcome message using the student_name
#specified in the route. The route should render the template 'welcome.html'.


@app.route("/roster/<string:student_name>/<int:grade_view>")
def roster(student_name, grade_view):
    class_roster = [
        ("Moana", 100, Senior),
        ("Belle", 89, Freshman),
        ("Daphne", 71, Sophomore),
        ("Ariel", 55, Freshman),
        ("Ana", 82, Senior),
        ("Pocahontas", 92, Junior),
        ("Aurora", 95, Junior)
    ]
    return render_template('roster.html', student_name=student_name, class_roster=class_roster, standing=standing)

#@app.route("/roster/<string:student_name>/<int:grade_view>")
#def roster(student_name, grade_view):
#    class_roster = [
#        ("Moana", 100, Senior),
#        ("Belle", 89, Freshman),
#        ("Daphne", 71, Sophomore),
#        ("Ariel", 55, Freshman),
#        ("Ana", 82, Senior),
#        ("Pocahontas", 92, Junior),
#        ("Aurora", 95, Junior)
#    ]
#    return render_template('roster.html', student_name=student_name, class_roster=class_roster, grade_view=grade_view)
#'/roster/' : To implement this route you need to first define a global variable that stores a
#elements; a student's name, a student's grade and a student's class standing (i.e.
#'Freshman', 'Sophomore', junior', 'Senior'). Populate this variable with student information
#(create at least 7 student entries.
