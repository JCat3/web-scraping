#!/usr/bin/env python
# coding: utf-8

# # Nasa Mars News


#dependencies
import os
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def scrape_info():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    #URL to be scraped
    url ='https://redplanetscience.com/'
    browser.visit(url)


    #retrieve page with the results module
    html = browser.html


    #create beautiful soup object; parse with html.parser
    soup = bs(html, 'html.parser')


    #print bs object
    print(soup.prettify())


    results = soup.find('div', class_="content_title")
    print(results)



    #store thread title
    news_title = results.text
       
    print(news_title)



    #title element is class = "card-text" 
    p_results = soup.find('div', class_="article_teaser_body")
    print(p_results)

    #store thread title
    news_p = p_results.text
       
    rint(news_p)

    # # JPL Mars Space Images - Featured Image

    #URL to be scraped
    space_url = 'https://spaceimages-mars.com/'
    browser.visit(space_url)


    #retrieve page with the results module
    space_html = browser.html

    #create beautiful soup object; parse with html.parser
    soup = bs(space_html, 'html.parser')

    #print bs object
    print(soup.prettify())

    image_results = soup.find('a', class_="fancybox-thumbs")
    print(image_results)

    # save Image URL 
    base_url = 'https://'
    featured_image = image_results.get('href')

    featured_image_url = base_url + featured_image
       
    print(featured_image_url)


    # # Mars Facts

    #URL to be scraped
    mars_url = 'https://galaxyfacts-mars.com/'

    #read in tables
    mars_tables = pd.read_html(mars_url)
    mars_tables

    # convert table to df
    mars_df = mars_tables[0]
    mars_df.head()

    #df to html
    html_mars = mars_df.to_html()
    html_mars


    # # Mars Hemispheres

    #URL to be scraped
    hemisphere_url = 'https://marshemispheres.com/'
    browser.visit(hemisphere_url)

    #retrieve page with the results module
    hemisphere_url = browser.html

    #create beautiful soup object; parse with html.parser
    soup = bs(hemisphere_url, 'html.parser')


    #print bs object
    print(soup.prettify())


    hemi_info = soup.find_all('div', class_="item")
    print(hemi_info[0])


    hemisphere_title= hemi_info[0].find('h3').text
    print(hemisphere_title)

    #hemisphere_image = soup.find_all('a', class_="itemLink product-item")

    image_url= hemi_info[0].find('img', class_="thumb").get('src')
    print(image_url)


    import time
    #results returned as iterable list
    hemisphere_info = soup.find_all('div', class_="item")

    mars_hemisphere_images = []

    #loop through returned results
    for x in range(4):
        #html object
        html = browser.html
        #parse HTML with bs
        soup = bs(hemisphere_url, 'html.parser')
        #retrieve all elements with hemisphere title & URL
        titles = soup.find_all('div', class_="item")
        time.sleep(10)
    
        #iterate through Mars Hemisphere info
        for title in titles:
            hemisphere_title= title.find('h3').text
            part_url = title.find('img', class_="thumb").get('src')
            image_url= "https://marshemispheres.com/" + part_url
        
            mars_dictionary = {'title': hemisphere_title, "image_url": image_url}
            mars_hemisphere_images.append(mars_dictionary)
    browser.back()
    
    print(mars_hemisphere_images)

    # store data in a dictionary

    mars_data = {
        "news-title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "html_mars": html_mars,
        "mars_hemisphere_images": mars_hemisphere_images 
    }

    browser.quit()

    return mars_data

