import requests
from bs4 import BeautifulSoup
index_empty_count = 0
print("Welcom to My Scrapping Application using Beautiful Soup")
url = input("Enter the website url : ")
tag = input("Enter the tag you want to scrap : ")
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    tag_with_value = soup.find_all(tag)
    if tag_with_value:
        print(f"\n I found almost {len(tag_with_value)} {tag} :")
        for index, value in enumerate(tag_with_value, 1):
            if value.text.strip():
                print(f"{index} : {value.text.strip()}\n")
            else:
                index_empty_count +=1
                continue
    else:
        print(f"Sorry!!! . The {tag} is not present in the website.")
else:
    print(f"Failed to retrieve html from the website. Error Status Code : {response.status_code}")
print(f"The total number of tags which contains no content is {index_empty_count}")
    
