import unittest

from ..checkers.email_checker import email_checker, company_email_finder


class TestEmailChecker(unittest.TestCase):
    def setUp(self):
        self.list_of_emails = [
            'aardwolfarchers@gmail.com', 'aardwolfarchers@gmail.com', 'aardwolfarchers@gmail.com', 'aardwolfarchers@gmail.com',
            'aardwolfarchers@gmail.com', 'info@pindersschoolwear.co.ukwww.pindersschoolwear.com', 'aardwolfarchers@gmail.com',
            'aardwolfarchers@gmail.com', 'aardwolfarchers@gmail.com', 'aardwolfarchers@gmail.com', 'aardwolfarchers@gmail.com',
            'aardwolfarchers@gmail.com', 'aardwolfarchers@gmail.com', 'aardwolfarchers@gmail.com', 'aardwolfarchers@gmail.com',
            'aardwolfarchers@gmail.com', 'aardwolfarchers@gmail.com', 'info@pindersschoolwear.co.ukwww.pindersschoolwear.com',
            'aardwolfarchers@gmail.com', 'aardwolfarchers@gmail.com', 'aardwolfarchers@gmail.com', 'aardwolfarchers@gmail.com',
            'aardwolfarchers@gmail.com', 'aardwolfarchers@gmail.com',
        ]

    def test_valid_present_email(self):
        emails = [
            'https://aardwolfarchers.org.uk',
            'chris@nautoguide.com',
            '<EMAIL>'
        ]
        check = email_checker(emails, 'chris@nautoguide.com')
        self.assertEqual(True, check)  # add assertion here

    def test_nonsense_present_email(self):
        emails = [
            'https://aardwolfarchers.org.uk',
            'chris@nautoguide.com',
            '<EMAIL>'
        ]
        check = email_checker(emails, '<EMAIL>')
        self.assertEqual(False, check)

    def test_invalid_present_email(self):
        emails = [
            'https://aardwolfarchers.org.uk',
            'chris@nautoguide.com',
            '<EMAIL>'
        ]
        check = email_checker(emails, 'https://aardwolfarchers.org.uk')
        self.assertEqual(False, check)

    def test_valid_absent_email(self):
        emails = [
            'https://aardwolfarchers.org.uk',
            '<EMAIL>',
            '<EMAIL>'
        ]
        check = email_checker(emails, 'chris@nautoguide.com')
        self.assertEqual(False, check)

    def test_invalid_absent_email(self):
        emails = [
            '<EMAIL>',
            '<EMAIL>',
            '<EMAIL>'
        ]
        check = email_checker(emails, 'https://aardwolfarchers.org.uk')
        self.assertEqual(False, check)

    def test_present_email_finder(self):
        company_email_check = company_email_finder(self.list_of_emails)
        self.assertEqual('aardwolfarchers@gmail.com', company_email_check)

if __name__ == '__main__':
    unittest.main()
