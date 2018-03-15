"""Test module"""
import src.emailer as emailer
import os
import unittest

class TestEmailMethods(unittest.TestCase):
    TEST_FILE = None
    TEST_FILE_NAME = 'emails.txt'
    TEST_CONTENT = 'bob.smith@company.com\nbobby.joe@southern.com\n'

    def create_email_file(self):
        test_file = open(self.TEST_FILE_NAME, 'w+')
        test_file.write(self.TEST_CONTENT)
        test_file.close()

        return test_file

    def test_read_email_address(self):
        self.assertEqual(self.TEST_CONTENT.splitlines(), emailer.get_email_address(self.create_email_file()))
