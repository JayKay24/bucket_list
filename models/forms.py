import wtforms

class EntryForm(wtforms.Form):
    title = wtforms.StringField('Entry Name')
    status = wtforms.SelectField(
        'Entry status',
        choices=((True, 'Done'),
                 (False, 'Not Done')))