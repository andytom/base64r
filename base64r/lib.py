import os
import uuid
import base64

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


