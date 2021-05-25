from flask import render_template, flash, request, redirect, url_for
from gradgift.forms import NameForm
from gradgift import app

@app.route('/', methods=["GET", "POST"])
def index():
    """Display index (home) route."""
    form = NameForm(request.form)
    if request.method == 'POST':
        if form.validate():
            try:
                name = form.name.data
                name = name.lower()
                if name == "afeefah":
                    return redirect(url_for('afeefah'))
                elif name == "yara":
                    return redirect(url_for('yara'))
                else:
                    flash("Name not recognized. Please try again.", "warning")
                    return render_template("index.html", name_form = form)
            except:
                flash("Something went wrong. Please try again.", "warning")
                return render_template("index.html", name_form = form)
    return render_template('index.html', name_form = form)

@app.route('/afeefah')
def afeefah():
    return render_template('afeefah.html')

@app.route('/yara')
def yara():
    return render_template('yara.html')
