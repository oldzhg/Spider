import requests
from bs4 import BeautifulSoup

url = "https://ssb.solano.edu/PROD/SCC_FindAccount_2.P_ValidateMe"
data = {'fname_in': 'Joshua', 'lname_in': 'Valdez', 'dob_in': '08021997', 'last4ssn_in': '0822'}

response = requests.post(url, data=data, verify=False)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.find_all("td", class_="PlainTxt")[0].string)


