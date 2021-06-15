from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import html_text

def mars_news(browser):
    url = "https://redplanetscience.com"
    browser.visit(url)
    
    html = browser.html
    soup = bs(html, "html.parser")
    
    news_title = soup.find('div', class_='content_title').text

    news_p = soup.find('div', class_='article_teaser_body').text

    return news_title, news_p


def image_scrape(browser):
    
    featured_image_url = 'https://spaceimages-mars.com/'
    browser.visit(featured_image_url)
    image_button = browser.find_by_tag("button")[1]
    image_button.click()
    
    html = browser.html
    soup = bs(html, "html.parser")

    mars_image = soup.find('img', class_= 'fancybox-image').get('src')

    return featured_image_url + mars_image

def mars_facts():
    df = pd.read_html("https://galaxyfacts-mars.com")[0]
    
    df.columns = ['Description','Mars', 'Earth']
    
    df.set_index('Description', inplace = True)
    
    return df.to_html(classes = "table table-striped")



def hemisphere(browser):
    url ='https://marshemispheres.com/'

    browser.visit(url +'index.html')
    title=[]
    sample = []

    html = browser.html
    soup = bs(html, "html.parser")

   
    for i in range(4):    
        image_button = browser.find_by_tag("a.product-item img")[i].click()
        word = soup.find('h2', class_='title').
        title.append(word)
        pictures = soup.find('img', class_ ="thumb").get('src')
        sample.append(pictures)
        browser.back()

    
    title_1 = title[0]
    title_2 = title[1]
    title_3 = title[2]
    title_4 = title[3]

    Im_1 = url + sample[0] 
    Im_2 = url + sample[1]
    Im_3 = url + sample[2]
    Im_4 = url + sample[3]
        
    return Im_1, Im_2, Im_3, Im_4, title_1, title_2, title_3, title_4
    


def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    news_title,news_p = mars_news(browser)
    mars_image= image_scrape(browser)
    table = mars_facts()
    Im_1, Im_2, Im_3, Im_4, title_1, title_2, title_3, title_4= hemisphere(browser)
    
    


 
    news_data = {
        
        "news_tile": news_title,
        "news_p":news_p,
        "mars_image": mars_image,
        "table":table,
        "title_1":title_1,
        "title_2":title_2,
        "title_3":title_3,
        "title_4":title_4,
        "Im_1": Im_1,
        "Im_2": Im_2,
        "Im_3": Im_3,
        "Im_4": Im_4,

        #"title": title
        
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return news_data






