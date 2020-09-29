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
user_name = input("Hey! What's your name? ")

################################################################################################
# function for correction
# true or false to return next set of questions
def ask_and_confirm(__ask, var_name):
    # __ask
    while __ask == Y or __ask == y:
        if __ask == True: # Yes
            print("Awesome! "+var_name+", will help us connect relative links in the website if you decide to scrape them too!")
    while __ask == N or __ask == n:
        if __ask == False: # No, reask
            var_name = input("Whoops! What's is the base link again? ")
    return var_name
################################################################################################

base_url__ask = False

#######
####### Hi [user_name]! So what's the website you want to scrape?
websiteurl = input("Hi "+user_name+"! So what's the website you want to scrape? ")
# Great! Can you specify the static part of your website for us?
# E.g. if your website was http://foo.com/recipes01.html you would enter http://foo.com/
# Anther example. If your website was http://calvin.com/staff/staffpage01.html you would enter http://calvim.com/staff/
print('Great! Can you specify the static part of your website for us?')
print('E.g. if your website was http://foo.com/recipes01.html you would enter http://foo.com/')
print('Anther example. If your website was http://calvin.com/staff/staffpage01.html you would enter http://calvim.com/staff/')
# Enter your links' base url:
base_url = input("Enter your links' base url: ")
# Lets make sure everything was typed correctly, is this correct: [base_link] - [Y][N]
## base_url__ask = input("Lets make sure everything was typed correctly, is this correct: "+base_url+" - [Y][N]")
## [Y] 
## base_url__ask == True # Yes
# Awesome! [base_link][5:].., will help us connect relative links in the website if you decide to scrape them too!
## [N]
## base_url_ask == False # No, reask
# Whoops! What's is the base link again?
base_url = ask_and_confirm(base_url__ask, base_url)
# Awesome! [base_link][5:].., will help us connect relative links in the website if you decide to scrape them too!



################################################################################################
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

print("Okay, websiteurl[10:].., lets specifcy where we're looking. ")
print("What is the element type we're looking for in the page? ")
print("The most common type of element would be a div, and we're looking at divs by default. ")
print("If you want to change this Press N. Otherwise, would you like to continue "+user_name+"? - [Y, Continue][N, Change] ")

### [Y]
base_element = 'div'
### [N]
## Please type the element name:
base_element = input("Please type the element name: ")

collection__type = 'Id or Class not set correctly'
# if collection__type is not set_id or is not set_class: 
# Is it an [#id] or [.class]?
if base_element == base_id:
    collection__type = set_id
# Cool, so it's an Id, what's the id's name?:
id_name = input("Cool, so it's an Id, what's the id's name?: ")
## [user_name], lets make sure. Is this correct: [#][id_name] - [Y][N]
### [Y]
## Excellent, lets continue. >
### [N]
## Lets fix it, enter the id name:
id_name =input("Lets fix it, enter the id name: ")
## Excellent, lets continue. >

if base_element == base_class:
    collection__type = set_class
# Cool, so it's a Class, what's the class's name?
class_name = 2
print("[user_name], let's make sure. Is this correct: [.][class_name] - [Y][N]")
### [Y]
## Excellent, lets continue. >
print("Excellent, lets continue. >")
### [N]
## Lets fix it, enter the class name:
## [user_name], let's make sure. Is this correct: [.][class_name] - [Y][N]
### [Y]
## Excellent, lets continue. >
print("Excellent, lets continue. >")
### [N]
## Lets fix it, enter the class name:
class_name = 2
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
if inner_element == headings:
    if collection__type == set_id or collection__type == set_class:
        collect_links = collection_id.findAll('h1')
    
if inner_element == links:
    if collection__type == set_id:
        collect_links = collection_id.findAll('a', href=True)
        for link in collect_links:
            if link['href']:
                relative = link['href']
                collection_list.append(urljoin(base_url, relative))
#    else:
#        continue

    if collection__type == set_class:
        collect_links = collection_class.findAll('a', href=True)
        for link in collect_links:
            if link['href']:
                relative = link['href']
                collection_list.append(urljoin(base_url, relative))
#    else:
#        continue
        
#if inner_element == span:
#    skip
#if inner_element == text:
#    skip
#if inner_element == bold_text:
#    skip
#if inner_element == italic_text:
#    skip
#if inner_element == another_oct_id:
#    skip
#if inner_element == another_dot_class:
#    skip
#if inner_element == everything:
#    skip
    
################################################################################################
################################################################################################


