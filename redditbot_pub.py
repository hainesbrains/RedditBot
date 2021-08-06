import requests
import json

client_id = "INSERT_ID"
token = "INSERT_TOKEN"
username = "INSERT_USERNAME"
password = "INSERT_PASSWORD"
botname = "INSERT_BOTNAME"

auth = requests.auth.HTTPBasicAuth(client_id, token)
data = {"grant_type": "password","username": username,"password": password}


headers = {"User-Agent": botname+"/0.0.1"}
request = requests.post("https://www.reddit.com/api/v1/access_token", auth=auth, data=data, headers=headers)
TOKEN = request.json()["access_token"]
headers = {**headers, **{"Authorization": f"bearer {TOKEN}"}}


while True:
    #User input
    print("Search Type (c to exit)")
    print("1. User")
    print("2. Subreddit")
    search_type = input()
    if search_type == "c":
        break
    print("User/Subreddit name")
    search = input()


    #Request
    if search_type == "1":
        req = requests.get("https://oauth.reddit.com/u/" + search, headers=headers)
    elif search_type == "2":
        req = requests.get("https://oauth.reddit.com/r/" + search, headers=headers)
    else:
        print("Error")
        input("Press enter to continue")
        continue


    #Saving to file
    print("Download file name")
    name = input()
    print("Text-only? (y/n)")
    formatted = input()
    if formatted == "y":
        export = open(name + ".txt", "a")
        for i in req.json()["data"]["children"]:
            if i["kind"] == "t3":
                export.write(i["data"]["selftext"])
        export.close()
    elif formatted == "n":
        export = open(name + ".txt", "w")
        export.write(json.dumps(req.json()))
        export.close()
    else:
        print("Error")
        input("Press enter to continue")
        continue
