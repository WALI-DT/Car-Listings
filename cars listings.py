import requests
from bs4 import BeautifulSoup
import pandas


baseurl = 'https://www.cars45.com'

headers = headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

r = requests.get('https://www.cars45.com/listing', headers=headers)

print(r.status_code)

soup = BeautifulSoup(r.content, 'lxml')
productlist = soup.find_all("section", class_='cars-grid grid')


linklist = []
for item in productlist:
    for link in item.find_all("a", href=True):
        linklist.append(baseurl + link['href'])


linklist = []
for x in range(1,42):
    r = requests.get(f'https://www.cars45.com/listing?page={x}', headers=headers)
    
soup = BeautifulSoup(r.content, 'lxml')
productlist = soup.find_all("section", class_='cars-grid grid')
    
for item in productlist:
    for link in item.find_all("a", href=True):
        linklist.append(baseurl + link['href'])
# len(linklist)


listed_cars = []
for link in linklist:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, "lxml")
    try:
        location = soup.find("p", class_="main-details__region").get_text(strip=True)
    except:
        location = "not specified"

    try:
        name = soup.find("div", class_="main-details__name").text.split("₦")[0]
    except:
        name = "N/A"
    
    try:
        price ='₦' + soup.find("div", class_="main-details__name").text.split("₦")[1].strip()
    except:
        price = "N/A"
    
    main_details = soup.find("div", class_="main-details__tags flex wrap")
    try:
        span_tags = main_details.find_all('span')
    except:
        pass
    try:
        use_history = span_tags[0].get_text(strip=True)
    except:
        pass
    try:
        milage = span_tags[-1].get_text(strip=True)
    except:
        pass
    try:    
        transmission = span_tags[1].get_text(strip=True) 
    except:
        pass
        
    car_details = {
        "location" : location,
        "name" : name,
        "price" : price,
        "use_history" : use_history,
        "milage" : milage,
        "transmission" : transmission
        } 
    listed_cars.append(car_details)
print("completed")
# len(listed_cars)

df = pandas.DataFrame(listed_cars)
# print(df)

df.to_csv(r"C:\Users\VICKY COMPUTERS\Desktop\web scraping projects\cars_listing.csv")