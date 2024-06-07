import requests

# Enter the website's link you want to check after webinstance.
webinstance = "https://www.smartschool.be/"

getweb = requests.get(webinstance)
print("Press 'ENTER' to receive status of:\n", webinstance,'\n')
input()
print(getweb.status_code)
