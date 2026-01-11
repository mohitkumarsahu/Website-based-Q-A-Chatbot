import requests
from bs4 import BeautifulSoup

def fetch_website(url:str)->str:
    response=requests.get(url,timeout=10)
    response.raise_for_status()
    return response.text



#res=fetch_website("https://www.nic.gov.in/personal-education-number/")


def extract_text(html:str):                 # Get all text and remove extra spaces and lines and return clean text and title.
    soup=BeautifulSoup(html, "html.parser") #Making page, structured so python can read it easily.
   
    for tag in soup(["script", "style", "nav", "header", "footer"]):
        tag.decompose()
    
    
    title=soup.title.string if soup.title else ""   # extracting title of the page

    clean_line=[]

    for line in soup.get_text().splitlines():
        stripped=line.strip()

        if stripped:
            clean_line.append(stripped)

    
    text='\n'.join(clean_line)

    return title, text
    

