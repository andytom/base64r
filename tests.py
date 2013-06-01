import unittest
import os
import shutil
import base64

import base64r.lib


#-----------------------------------------------------------------------------#
# Test Cases
#-----------------------------------------------------------------------------#
class LibTestCase(unittest.TestCase):
    """Tests to test the libary functions"""
    def setUp(self):
        self.dir = '/tmp/base64r/test/'
        self.file = 'test_file'
        self.fullpath = os.path.join(self.dir, self.file)
        self.string = 'A Test String'

    def tearDown(self):
        self._rmdir()

    def _rmdir(self):
        shutil.rmtree(self.dir, ignore_errors=True)

    def test_ensure_dir(self):
        self.assertFalse(os.path.exists(self.dir))
        base64r.lib.ensure_dir(self.fullpath)
        self.assertTrue(os.path.exists(self.dir))

    def test_base64_decode(self):
        encoded_data = base64.b64encode(self.string)
        result = base64r.lib.base64_decode(encoded_data, 'txt', self.dir)
        with open(result['fullpath'], 'r') as f:
            self.assertEqual(f.read(), self.string)


#-----------------------------------------------------------------------------#
if __name__ == '__main__':
    unittest.main()
