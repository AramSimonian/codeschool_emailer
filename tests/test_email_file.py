"""Test module"""
import src.emailer as emailer
import os
import unittest

class TestEmailMethods(unittest.TestCase):
    TEST_FILE_NAME = 'testfile.txt'
    TEST_EMAIL_CONTENT = 'bob.smith@company.com,Bob Smith\nbobby.joe@southern.com,Bobby Joe\n'
    TEST_EMAIL_RESULT = {'bob.smith@company.com':'Bob Smith','bobby.joe@southern.com':'Bobby Joe'}
    TEST_SCHEDULE_CONTENT = 'Some event - 09:00'

    def create_test_file(self, content):
        test_file = open(self.TEST_FILE_NAME, 'w+')
        test_file.write(content)
        test_file.close()

        return test_file

    def test_get_email_address(self):
        self.assertEqual(self.TEST_EMAIL_RESULT
            , emailer.get_email_address(self.create_test_file(self.TEST_EMAIL_CONTENT)))

    def test_get_schedule(self):
        self.assertEqual(self.TEST_SCHEDULE_CONTENT
            , emailer.get_schedule(self.create_test_file(self.TEST_SCHEDULE_CONTENT)))
