"""
author = Bhavya
"""
import json
import webbrowser
import requests

def randomart():
    '''

    To display and open a random wikipedia article

    '''
    url = 'https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json'
    url_1 = 'https://en.wikipedia.org/wiki?curid='
    res = requests.get(url)
    data = res.json()
    print('===========================================')
    print('Welcome to the Game: Reading Random Wikipedia Articles')
    print('===========================================')
    k = 0
    if k == 0:
        print("*********************************************************")
        print('List of Random Articles :')
    while k < 10:
        print(k+1, data["query"]["random"][k]["title"])
        k += 1
    interest = "yes"
    while(interest == "yes"):
        y = int(input("Enter the Article number you are interested in: "))
        x = y-1

        if x>=0 and x<10:
            article_id = data["query"]["random"][x]["id"]
            print('Opening browser....')
            url_2 = url_1 + str(article_id)
            webbrowser.open(url_2, new=2)
        else:
            print("Enter a valid article number!!")
        interest = input("Interested in same article list ? yes/no : ")
    
    per = input("Want to refresh this list or quit the game? refresh/quit : ")
    if per.lower() == "refresh":
        randomart()
    else:
        print('===========================================')
        print("Thank you for playing!!")
        print('===========================================')

        


randomart()
