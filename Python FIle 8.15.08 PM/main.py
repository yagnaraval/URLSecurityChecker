import json
import requests
#from bs4 import BeautifulSoup

class yagna():
    print("\n\n")
    user="ravalyagna"
    password="ray"
    enter1=input("Enter USer Name: ")
    enter2=input("Enter Password: ")
    print("\n\n")
    if(enter1==user and enter2==password):
        print("\n\n")
        a=input("Enter Url of Website: ")
        indicators={
            a
        }
        url='https://www.virustotal.com/vtapi/v2/url/report'

        #api='b780c8dd0551e47e19c0be0f0cedcc819e8322beea6d6380c8ee2c48de354d37'
        api='4551455292a1e79fb67d7c646a9ffe024c770fc8390cdc08f80eda5a5289aae9'

    else:
        print("Wrong UserName or Password")
    