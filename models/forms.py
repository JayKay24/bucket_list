import wtforms

class EntryForm(wtforms.Form):
    title = wtforms.StringField('Entry Name')
    status = wtforms.SelectField(
        'Entry status',
        choices=((True, 'Done'),
                 (False, 'Not Done')))
                 
class UserForm(wtforms.Form):
    first_name = wtforms.StringField('First Name')
    last_name = wtforms.StringField('Last Name')
    password = wtforms.PasswordField('Password')