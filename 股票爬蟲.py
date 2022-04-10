import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.yuanta.com.tw/eYuanta/securities/Node/Index?MainId=00430&C1=2018040402289271&C2=2018040402339283&ID=2018040402339283&Level=2&rnd=93882")
soup = BeautifulSoup(response.text, "html.parser")

result = soup.prettify()
#result = soup.find_all("td",class_ = "t3t1")
print(result)

