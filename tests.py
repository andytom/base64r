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

    def test_create_filename(self):
        file_1 = base64r.lib.create_filename('txt')
        file_2 = base64r.lib.create_filename('txt')
        self.assertNotEqual(file_1, file_2)

    def _run_extention_test(self, filename, result):
        with open(filename, 'rb') as f:
            ext = base64r.lib.guess_extention(f.read())
        self.assertEqual(ext, result)

    def test_guess_extention_txt(self):
        self._run_extention_test("resources/example.txt", '.txt')

    def test_guess_extention_pdf(self):
        self._run_extention_test("resources/example.pdf", '.pdf')

    def test_guess_extention_doc(self):
        self._run_extention_test("resources/example.doc", '.doc')

    @unittest.skip("Magic picks this up as a zip file.")
    def test_guess_extention_docx(self):
        self._run_extention_test("resources/example.docx", '.docx')


#-----------------------------------------------------------------------------#
if __name__ == '__main__':
    unittest.main()
