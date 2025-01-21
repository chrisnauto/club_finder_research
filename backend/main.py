from checkers.email_checker import *
from utils.web_scraper import *


#Validiates given email against the sites text
def email_check(site_url, company_email, file_addr) -> (bool, str):
    list_of_urls = get_links(site_url)

    with open(file_addr, "w") as file:
        for site in list_of_urls:
            formatted_string = format_string(get_site_text(site) + "\n\n")
            file.write(formatted_string)

    list_of_emails = email_finder(file_addr)
    if company_email == "":
        company_email = company_email_finder(list_of_emails)
        print("Company email has been updated")
        is_email_correct = True
    else:
        is_email_correct = email_checker(list_of_emails, company_email)

    return is_email_correct, company_email