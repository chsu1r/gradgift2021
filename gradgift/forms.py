from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError, Email
from wtforms.widgets import TextArea

class NameForm(FlaskForm):
    """Form for login."""
    name = StringField('your first name', render_kw={"placeholder": "your first name"},
                        validators=[DataRequired()])
    submit = SubmitField('Submit')
