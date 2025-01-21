import os
import re
import requests
from requests.exceptions import MissingSchema

from bs4 import BeautifulSoup


#Scrapes given site for all text available
def get_site_text(url) -> str:
    try:
        response = requests.get(url)
    except MissingSchema:
        return ""

    soup = BeautifulSoup(response.text, 'html.parser')

    return soup.get_text()


#Gets all links from a website and returns the list
def get_links(url) -> list[str]:
    try:
        response = requests.get(url)
    except MissingSchema:
        return [""]

    soup = BeautifulSoup(response.text, 'html.parser')

    urls = [url]
    for link in soup.find_all('a'):
        if link not in urls:
                urls.append(link.get('href'))

    return urls


#Formats web text to be separated by a linebreak rather then an arbitrary number of blank lines
def format_string(string) -> str:
    string = string.strip()
    string = os.linesep.join([s for s in string.splitlines() if s])
    return string


#Finds all email addresses on the website
def email_finder(file_addr) -> list[str]:

    with open(file_addr, "r") as file:
        emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", file.read())

        return emails