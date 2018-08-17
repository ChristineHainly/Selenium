# Facebook Selenium Script

This is a short and simple script that will allow a user to login to their facebook account. 

## Getting Started

Make sure you have Python and Selenium installed on your local machine. Once these two items are installed you can start working on running the selenium script. For help on installing Python and Selenium follow the step by step tutorial titled Python_and_Selenium_Documentation.docx

### Prerequisites

* Selenium
* Python
* Webdriver for your browser
* Facebook account login information
* Update the following lines with the correct login information 
** (To secure this put the login information in a separate file and have the script read the user information from it. This way the login information is not in plain text in the script.

```
self.email_field.send_keys('updateThisToTheCorrectEmail@something.com')
self.password_field.send_keys('updateThisToTheCorrectPassword')
```

## Deployment

To run this script, open the command line and navigate to the file with the facebook_login.py file in it and run the following command:

```
python facebook_login.py
```

## Authors

* **Christine Hainly**
