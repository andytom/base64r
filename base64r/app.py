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
from flask import Flask, render_template, flash, abort, send_from_directory
from base64r.forms import decode_form
from base64r.lib import base64_decode

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
        # valid base64.
        try:
            written_file = base64_decode(form.content.data,
                                         app.config['OUTPUT_FOLDER'],
                                         form.ext.data
                                         )
            filename = written_file['filename']
            flash("File Scuessfully decoded", "alert-success")
            return render_template('download.html', filename=filename)
        except:
            flash("Unable to decode the string", "alert-error")

    return render_template('index.html', form=form)


@app.route('/downloads/<path:filename>')
def download(filename):
    """Handle downloads when not being run behind a Web Server."""
    if app.config['DEBUG']:
        # From my testing this should safely handle filename if someone
        # includes a "../" or something similar however might be worth a
        # second look.
        return send_from_directory(app.config['OUTPUT_FOLDER'], filename)
    abort(500)
