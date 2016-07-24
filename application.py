from flask import Flask, render_template, request, redirect
# from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""

    return redirect("/application-form")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application-form")
def application_page():
    """Serve and take submission of the application form."""
    return render_template("application-form.html")

# I would have preferred to use the application route to redirect to the 
# application-response route but I couldn't figure out how to pass the 
# arguments in a redirect with a POST request
@app.route("/application", methods=["POST"])
def application_submission():
    """Handle form submission and render the response page."""
    # firstname = firstname
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    jobappliedfor = request.form.get("jobappliedfor")
    salaryrequirement = request.form.get("salaryrequirement")
    # trying to create a workaround to handle people accessing the
    # application page directly (meaning no parameters are passed)
    # ideas on lines 33/41/42, and 43/44
    # if firstname == "firstname":
    #     return redirect("/application-form")
    # if not request.form.get("firstname")
    #     return redirect("/application-form")
    return render_template("application-response.html", firstname=firstname,
        lastname=lastname, jobappliedfor=jobappliedfor,
        salaryrequirement=salaryrequirement)

# @app.route("/application-response")
# def application_confirmation():
#     """Return an application acknowledgement."""
#     return render_template("application-response.html")

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    # app.debug = True

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

