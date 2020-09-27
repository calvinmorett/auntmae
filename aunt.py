from bs4 import BeautifulSoup
import requests
from datetime import datetime
from urllib.parse import urljoin

# ask questions
# change variables in the next sections
# use those variables to change outcomes in what is being scraped
# if there are mistakes, catch them

#######
####### Hey! What's your name?
user_name =

#######
####### Hi [user_name]! So what's the website you want to scrape?
websiteurl = 'https://....'
# Great! Can you specify the static part of your website for us?
# E.g. if your website was http://foo.com/recipes01.html you would enter http://foo.com/
# Anther example. If your website was http://calvin.com/staff/staffpage01.html you would enter http://calvim.com/staff/
# Enter your links' base url:
base_url = 'https://....'
# Lets make sure everything was typed correctly, is this correct: [base_link] - [Y][N]
## [Y] 
# Awesome! [base_link][5:].., will help us connect relative links in the website if you decide to scrape them too!
## [N]
# Whoops! What's is the base link again?
base_url =
# Awesome! [base_link][5:].., will help us connect relative links in the website if you decide to scrape them too!

################################################################################################
################################################################################################

# global relative
r = requests.get(websiteurl)
soup = BeautifulSoup(r.text, 'html.parser')

################################################################################################
################################################################################################

#######
####### Okay, websiteurl[10:].., lets specifcy where we're looking. 
# What is the element type we're looking for in the page?
# The most common type of element would be a div, and we're looking at divs by default.
# If you want to change this Press N. Otherwise, would you like to continue [user_name]? - [Y, Continue][N, Change]
### [Y]
base_element = 'div'
### [N]
## Please type the element name:
base_element = 

collection__type = 'Id or Class not set correctly'
# if collection__type is not set_id or is not set_class: 
# Is it an [#id] or [.class]?
if id :
    collection__type = set_id
# Cool, so it's an Id, what's the id's name?:
id_name =
## [user_name], lets make sure. Is this correct: [#][id_name] - [Y][N]
### [Y]
## Excellent, lets continue. >
### [N]
## Lets fix it, enter the id name:
id_name =
## Excellent, lets continue. >

if class:
    collection__type = set_class
# Cool, so it's a Class, what's the class's name?
class_name =
## [user_name], let's make sure. Is this correct: [.][class_name] - [Y][N]
### [Y]
## Excellent, lets continue. >
### [N]
## Lets fix it, enter the class name:
class_name =
## Excellent, lets continue. >

################################################################################################
################################################################################################

collection_list = []

if collection__type == set_id:
    collection_id = soup.find(base_element, {"id": id_name})
if collection__type == set_class:
    collection_class = soup.find(base_element, {"class": class_name})

################################################################################################
################################################################################################

#######
####### Lets continue! So we're looking at [#id]_[.class], what do we need from there?
# [headings][links][span][text][bold text][italic text][another id][another class][everything]
if headings:
    collection_type
if links:
    if collection__type == set_id:
        collect_links = collection_id.findAll('a', href=True)
        for link in collect_links:
            if link['href']:
                relative = link['href']
                collection_list.append(urljoin(base_url, relative))
    else:
        continue

    if collection__type == set_class:
        collect_links = collection_class.findAll('a', href=True)
        for link in collect_links:
            if link['href']:
                relative = link['href']
                collection_list.append(urljoin(base_url, relative))
    else:
        continue
if span:
if text:
if bold_text:
if italic_text:
if another oct_id:
if another dot_class:
if everything:
    
################################################################################################
################################################################################################


