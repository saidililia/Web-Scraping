import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
import pandas as pd

driver_service = Service(executable_path=r"C:\Users\Lilia\Desktop\WebScraping\chromedriver.exe")
driver = Chrome(service=driver_service)

def get_URLs(Email, Title):
 graphql_url = "https://api.ouedkniss.com/graphql"
 i = 0

 for page in range(1,25):

    events_payload = {
        "operationName": "SearchQuery",
        "variables": {
            "mediaSize": "MEDIUM",
            "q": None,
            "filter": {
                "categorySlug": "services-evenements-divertissement",
                "origin": None,
                "connected": False,
                "delivery": None,
                "regionIds": [],
                "cityIds": [],
                "priceRange": [None, None],
                "exchange": False,
                "hasPictures": False,
                "hasPrice": False,
                "priceUnit": None,
                "fields": [],
                "page": page,
                "count": 48,
                },
        },
        "query": "query SearchQuery($q: String, $filter: SearchFilterInput, $mediaSize: MediaSize = MEDIUM) {\n  search(q: $q, filter: $filter) {\n    announcements {\n      data {\n        ...AnnouncementContent\n        smallDescription {\n          valueText\n          __typename\n        }\n        noAdsense\n        __typename\n      }\n      paginatorInfo {\n        lastPage\n        hasMorePages\n        __typename\n      }\n      __typename\n    }\n    active {\n      category {\n        id\n        name\n        slug\n        icon\n        delivery\n        priceUnits\n        children {\n          id\n          name\n          slug\n          icon\n          __typename\n        }\n        specifications {\n          isRequired\n          specification {\n            id\n            codename\n            label\n            type\n            class\n            datasets {\n              codename\n              label\n              __typename\n            }\n            dependsOn {\n              id\n              codename\n              __typename\n            }\n            subSpecifications {\n              id\n              codename\n              label\n              type\n              __typename\n            }\n            allSubSpecificationCodenames\n            __typename\n          }\n          __typename\n        }\n        parentTree {\n          id\n          name\n          slug\n          icon\n          children {\n            id\n            name\n            slug\n            icon\n            __typename\n          }\n          __typename\n        }\n        parent {\n          id\n          name\n          icon\n          __typename\n        }\n        __typename\n      }\n      count\n      __typename\n    }\n    suggested {\n      category {\n        id\n        name\n        slug\n        icon\n        __typename\n      }\n      count\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment AnnouncementContent on Announcement {\n  id\n  title\n  slug\n  createdAt: refreshedAt\n  isFromStore\n  isCommentEnabled\n  userReaction {\n    isBookmarked\n    isLiked\n    __typename\n  }\n  hasDelivery\n  deliveryType\n  likeCount\n  description\n  status\n  cities {\n    id\n    name\n    slug\n    region {\n      id\n      name\n      slug\n      __typename\n    }\n    __typename\n  }\n  store {\n    id\n    name\n    slug\n    imageUrl\n    __typename\n  }\n  user {\n    id\n    __typename\n  }\n  defaultMedia(size: $mediaSize) {\n    mediaUrl\n    __typename\n  }\n  price\n  pricePreview\n  priceUnit\n  oldPrice\n  priceType\n  exchangeType\n  __typename\n}\n",
    }

    event_resp = requests.post(graphql_url, json=events_payload).json()
    
    for event in event_resp['data']['search']['announcements']['data']:
        i = i + 1
        id = event['id']
        path = event['slug']
        url = path+'-d'+id
        title = event['title'].encode('utf-8')
        
        
        driver.get('https://www.ouedkniss.com/'+url)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        email = soup.find_all('span', class_='v-chip__content')
        n = email.__len__() - 1
        if n >1:
         print(title, ' | ',email[n].text)
         Email.append(email[n].text)
         Title.append(title)
         print('this is the email number: ', i)
        
    
def export_Excel(Email, Title):
    df = pd.DataFrame({'Tile': Title, 'Email': Email})
    df.to_csv('Ouedkniss/Email.csv')
    
    

if __name__=='__main__':
    Email = []
    Title = []
    get_URLs(Email, Title)
    print(Email,Title)
    export_Excel(Email=Email, Title=Title)
    pass 
