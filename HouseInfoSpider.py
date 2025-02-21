# -*- coding=utf-8 -*-
# version 1.1

import time
import requests
import pandas as pd
from bs4 import BeautifulSoup


def get_house(url):
    'get information of every house in page '
    information = {}    # save all information of house
    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"request failed: {e}")
        return None # when request failed , return None 
    # Get the house type, floor area, unit price, orientation, floor, and decoration status
    # houses = soup.select('.tab-cont-right .tr-line clearfix')
    # for house in houses:
    #     m = house.text.strip().split('\n')
    #     me = m[1]
    #     if '朝向' in me:
    #         me = me.strip('进门')
    #     if '楼层' in me:
    #         me = me[0:2]
    #     if '地上层数' in me:
    #         me = '楼层'
    #     if '装修程度' in me:
    #         me = '装修'
    #     information[me] = m[0].strip()

    # # Get the neighborhood name
    # name = soup.select('.rcont .blue')
    # information['小区名称'] = name[0].text

    # # Get the total price of the house
    # price = soup.select('.trl-item')
    # information['房屋总价'] = price[0].text
    # print(information)
    # return information

    # Mapping the keys for house information
    house_info_map = {
        '户型': 'trl-item1 w146',
        '建筑面积': 'trl-item1 w182',
        '单价': 'trl-item1 w132',
        '朝向': 'trl-item1 w146',
        '楼层': 'trl-item1 w182',
        '装修': 'trl-item1 w132',
    }


    # Extracting house details based on class names
    # for key, class_name in house_info_map.items():
    #     div = soup.find('div', class_=class_name)
    #     if div:
    #         value = div.find('div', class_='tt').text.strip()
    #         information[key] = value
    divs = soup.find_all('div', class_='trl-item1')     # get all div

    if len(divs) >= 6:
        information['户型'] = divs[0].find('div', class_='tt').text.strip() if divs[0].find('div', class_='tt') else 'Information is missing'
        information['建筑面积'] = divs[1].find('div', class_='tt').text.strip() if divs[0].find('div', class_='tt') else 'Information is missing'
        information['单价'] = divs[2].find('div', class_='tt').text.strip() if divs[0].find('div', class_='tt') else 'Information is missing'
        information['朝向'] = divs[3].find('div', class_='tt').text.strip() if divs[0].find('div', class_='tt') else 'Information is missing'
        information['楼层'] = divs[4].find('div', class_='tt').text.strip() if divs[0].find('div', class_='tt') else 'Information is missing'
        information['装修'] = divs[5].find('div', class_='tt').text.strip() if divs[0].find('div', class_='tt') else 'Information is missing'
    else:
        print("There is not enough data")

    # Get the neighborhood name
    name = soup.select('.rcont .blue')
    if name:
        information['小区名称'] = name[0].text.strip()
    
    # Get the total price of the house
    # price = soup.select('.price .newPrice')
    price = soup.select('.trl-item')
    # information['房屋总价'] = price[0].text
    if price:
        information['房屋总价'] = price[0].text.strip()
    else:
        information['房屋总价'] = "Information is missing"
    
    # Print and return the information
    print(information)
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    return information

# test function
# get_house("https://taiyuan.esf.fang.com/chushou/3_297109288.htm?channel=2,2&psid=1_1_60")   # url of every page


def get_page(i):
    'Paginate crawl data'
    url = r'https://taiyuan.esf.fang.com/house/i3{}/'.format(i) # Total number of pages
    res = requests.get(url)
    houses = BeautifulSoup(res.text, 'html.parser')
    # print(url)
    j = 1
    houses = houses.select('.shop_list .clearfix h4 a')
    page_information = []   # 数据存储
    for house in houses:
        try:
            demo_url = house['href']
            url = r'https://taiyuan.esf.fang.com' + demo_url + '?channe1=1,2&psid=1_{}_60'.format(j)    # How many houses are on each page
            # Get information about each house on the current page
            information = get_house(url)
            print('Crawling {} page {} house ...'.format(i, j), end='\r')
            page_information.append(information)
            j += 1
            time.sleep(5) # Prevent frequent crawling and prevent IP blocks from being blocked
        except Exception as e:
            print('->->->->->->->->->', e)
    # Convert the crawled data into DataFrame format
    df = pd.DataFrame(page_information)
    # de.to_csv('house_information.csv')
    return df
# get_page(1)


df = pd.DataFrame()  # create an empty DataFrame
name_csv = 'house_information_'
for i in range(1, 2): # A total of 100 pages of data were crawled
    try:
        df_get = get_page(i)
        # df = df.append(df_get)
        df = pd.concat([df, df_get], ignore_index=True)
        print(df)
    except Exception as e:
        print('->->->->->->->->->', e)
    if i/1 == 1:
        df.to_csv(name_csv + str(i) + '.csv')
        df = pd.DataFrame() # Clear the data that has been crawed to prevent memory overflow


        