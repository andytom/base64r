"""
    base64r
    =======

    base64r is a tool for dealing with base64 encoded strings.

    :copyright: (c) 2013 by Thomas O'Donnell.
    :license: BSD, see LICENSE for more details.
    :version: 0.1
"""
#-----------------------------------------------------------------------------#
# Setup
#-----------------------------------------------------------------------------#
from flask import Flask, render_template, send_file
from base64r.forms import decode_form
from base64r.lib import base64_to_stringio

app = Flask(__name__)
app.config.from_pyfile('main.cfg')


#-----------------------------------------------------------------------------#
# Routes
#-----------------------------------------------------------------------------#
@app.route('/', methods=['GET', 'POST'])
def index():
    """Index page for base64r"""
    form = decode_form()

    if form.validate_on_submit():
        # TODO
        # Write a custom validator for checking the contents of the data is
        # valid base64 string.
        strIO, filename = base64_to_stringio(form.content.data,
                                             form.filename.data)
        return send_file(strIO,
                         attachment_filename=filename,
                         as_attachment=True)

    return render_template('index.html', form=form)
