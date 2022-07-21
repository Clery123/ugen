import ugen
import unittest
import filecmp
import HtmlTestRunner
from io import StringIO
class UgenTests(unittest.TestCase):
    def test_main_no_file_input(self):
        #outfileTest = 'outputTest2.txt'
        outfile = 'output.txt'
        lst = ['--output',outfile]
        self.assertEqual(ugen.main(lst),"no input")

    def test_main_help(self):
        lst = ['-h']
        self.assertEqual(ugen.main(lst),"help")
    
    def test_main_multiple_files(self):
        outfileTest = 'outputTest1.txt'
        outfile = 'output.txt'
        infile1 = 'input1.txt'
        infile2 = 'input2.txt'
        lst = ['-o',outfile,infile1,infile2]
        ugen.main(lst)
        self.assertTrue(filecmp.cmp(outfile,outfileTest, shallow=False))
    
    def test_main_file_not_exist(self):
        outfile = 'output.txt'
        infile1 = 'input11.txt'
        self.assertEqual(ugen.write_output(outfile,infile1),"Does not exist")

    def test_generate_username_file_structure(self):
        outfile = 'output.txt'
        infile1 = 'input1_wrong.txt'
        lst = [outfile,infile1]
        self.assertEqual(ugen.generate_username(lst),"MatchError")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())
    