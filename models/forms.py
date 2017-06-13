import wtforms
from wtforms.validators import DataRequired

class EntryForm(wtforms.Form):
    """
    Class to generate an entry form.
    """
    title = wtforms.StringField('Entry Name', validators=[DataRequired()])
    status = wtforms.SelectField(
        'Entry status',
        choices=((True, 'Done'),
                 (False, 'Not Done')))
                 
class UserForm(wtforms.Form):
    """
    Class to generate a user form.
    """
    first_name = wtforms.StringField('First Name', validators=[DataRequired()])
    last_name = wtforms.StringField('Last Name', validators=[DataRequired()])
    password = wtforms.PasswordField('Password', validators=[DataRequired()])