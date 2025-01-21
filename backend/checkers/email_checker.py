from bs4 import BeautifulSoup
from validate_email import validate_email
import requests
import os
import re
from requests.exceptions import MissingSchema

#checks the email is real, and is on the website
def email_checker(emails, company_email) -> bool:

    valid_email = validate_email(
        company_email,
        check_format=True,
        check_blacklist=True,
        check_dns=True,
        dns_timeout=10,
        check_smtp=True,
        smtp_timeout=10
    )

    if not valid_email:
        print("email is invalid")
        return False

    if company_email not in emails:
        print("email not found on website")
        return False
    else:
        print("email is found on website")
        return True


#If there is no given email address, this will use the website to find the
# most likely address to be used instead
def company_email_finder(emails) -> str:
    # TODO just a temp solution, could also compare the company name to
    #  email to get most similar or ask an ai to guess which would be
    #  the most likely email
    most_common_email = max(set(emails), key=emails.count)
    print("Adding new email")

    return most_common_email