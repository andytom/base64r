"""
    base64r libs
    ============

    A libary containing helper functions for dealing with base64 decoding of
    files.

    :copyright: (c) 2013 by Thomas O'Donnell.
    :license: BSD, see LICENSE for more details.
    :version: 0.1
"""
import os
import uuid
import base64
import magic
import mimetypes


#-----------------------------------------------------------------------------#
# Files
#-----------------------------------------------------------------------------#
def create_filename(extention):
    """Create a unique filename with the passed extention."""
    random_string = str(uuid.uuid4())
    return '.'.join([random_string, extention])


def ensure_dir(filename):
    """Make sure that the passed directory containing the passed filename
    exists, create it if it does not."""
    dir = os.path.dirname(filename)
    if not os.path.exists(dir):
        os.makedirs(dir)


def write_file(bin_data, filename, directory):
    """Save the passed file as filename in the passed directory."""
    full_filename = os.path.join(directory, filename)
    ensure_dir(full_filename)
    with open(full_filename, 'wb') as f:
        f.write(bin_data)

    return {"filename": filename, "fullpath": full_filename}


def guess_extention(bin_data):
    mime_type = magic.from_buffer(bin_data, mime=True)
    if mime_type == 'text/plain':
        # mimetypes returns 'ksh' (or a huge list)
        return 'txt'
    ext = mimetypes.guess_extension(mime_type)
    if ext is None:
        # Default to 'dat' if we don't get anything
        ext = 'dat'
    return ext.replace('.', '')


def base64_decode(base64_string, directory, extention=None):
    """Decode the Base64 sting and write it to a file random named file with
       the passed extention in the passed directory.
    """
    bin_data = base64.b64decode(base64_string)
    if extention is None:
        extention = guess_extention(bin_data)
    filename = create_filename(extention)

    return write_file(bin_data, filename, directory)
