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
import StringIO
import magic
import mimetypes


#-----------------------------------------------------------------------------#
# Files
#-----------------------------------------------------------------------------#
def create_filename(extention):
    """Create a unique filename with the passed extention."""
    random_string = str(uuid.uuid4())
    return ''.join([random_string, extention])


def guess_extention(bin_data):
    mime_type = magic.from_buffer(bin_data, mime=True)
    ext_list = mimetypes.guess_all_extensions(mime_type)

    if len(ext_list) == 0:
        # Default to 'dat' if we don't get anything
        return 'dat'

    # Defult to the more common extentions when they are available
    # If not grab the first one available.
    if '.txt' in ext_list:
        ext = '.txt'
    else:
        ext = ext_list[0]

    return ext


def base64_to_stringio(base64_string, filename=''):
    """Decode the Base64 string and write it to a stringIO."""
    bin_data = base64.b64decode(base64_string)

    if filename == '':
        extention = guess_extention(bin_data)
        filename = create_filename(extention)

    strIO = StringIO.StringIO()
    strIO.write(bin_data)
    strIO.seek(0)

    return strIO, filename
