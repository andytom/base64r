"""
    base64r forms
    =============

    Forms for base64r.

    :copyright: (c) 2013 by Thomas O'Donnell.
    :license: BSD, see LICENSE for more details.
    :version: 0.1
"""
from flask_wtf import Form, TextField, Required, TextAreaField


#-----------------------------------------------------------------------------#
# Forms
#-----------------------------------------------------------------------------#
class decode_form(Form):
    content = TextAreaField('Base64',
                            validators=[Required()],
                            description="Base 64 encoded string to be decoded"
                            )
    filename = TextField('Filename',
                         description="The filename of the document"
                         )
