"""
    base64r
    =======

    base64r is a tool for dealing with base64 encoded strings.

    :copyright: (c) 2013 by Thomas O'Donnell.
    :license: BSD, see LICENSE for more details.
    :version: 0.1
"""
#------------------------------------------------------------------------------#
# Setup
#------------------------------------------------------------------------------#
import os
import uuid
import base64
import json

from flask import Flask, render_template, flash, abort, send_from_directory
from base64r.forms import decode_form

app = Flask(__name__)
app.config.from_pyfile('main.cfg')

#------------------------------------------------------------------------------#
# Helper Functions
#------------------------------------------------------------------------------#
def create_filename( extention ):
    """Create a random filename with the passed extention."""
    random_string = str( uuid.uuid4() )
    return '.'.join( [random_string, extention] )

def ensure_dir( filename) :
    """Make sure that the passed directory exists, create it if it does not."""
    dir = os.path.dirname(filename)
    if not os.path.exists( dir ):
        os.makedirs( dir )

def write_file( bin_data, filename, directory ):
    """Save the passed file as filename in the OUTPUT_FOLDER."""
    full_filename = os.path.join( directory, filename )
    ensure_dir( full_filename )

    # Write bin data
    with open( full_filename, 'wb' ) as f:
        f.write( bin_data )

    return {"filename" : filename, "fullpath" : full_filename }

def base64_decode( base64_string, extention, directory ):
    """Decode the Base64 sting and write it to a file random named file with
       the passed extention.
    """
    bin_data = base64.b64decode( base64_string )
    filename = create_filename( extention )

    return write_file( bin_data, filename, directory )

#------------------------------------------------------------------------------#
# Routes
#------------------------------------------------------------------------------#
@app.route( '/', methods=['GET', 'POST'] )
def index():
    form = decode_form()

    if form.validate_on_submit():
        try:
            written_file = base64_decode( form.content.data,
                                          form.ext.data,
                                          app.config['OUTPUT_FOLDER'] )
            filename = written_file['filename']
            flash( "File Scuessfully decoded", "alert-success" )
            return render_template( 'download.html',filename = filename )
        except:
            flash( "Unable to decode the string", "alert-error" )

    return render_template('index.html', form = form)

@app.route( '/downloads/<path:filename>' )
def download( filename ):
        return send_from_directory(app.config['OUTPUT_FOLDER'], filename )

