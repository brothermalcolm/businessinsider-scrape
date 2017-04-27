# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 17:13:55 2017

@author: SERNMO
"""

#%%
# Let’s start with the imports:
from lxml import html
import requests    
import pandas as pd
#%%
# Next we will use requests.get to retrieve the web page with our data, parse 
# it using the html module and save the results in tree:
page = requests.get('http://www.businessinsider.com/asian-hedge-funds-2011-5?IR=T&op=1&r=US&IR=T/#-ht-capital-management-hong-kong-1')
tree = html.fromstring(page.content)
#%%
# Knowing this we can create the correct XPath query and use the lxml xpath 
#function like this:
titles = tree.xpath('//h3[@class="slide-title"]/text()')
founded = tree.xpath('//div[@id]/p[1]/text()')
aum = tree.xpath('//div[@id]/p[2]/text()')
manager = tree.xpath('//div[@id]/p[3]/text()')
strategies = tree.xpath('//div[@id]/p[4]/text()')
#%%
#Let’s see what we got exactly:
print('title: ', titles)
print('founded: ', founded)
print('aum: ', aum)
print('manager: ', manager)
print('strategies: ', strategies)
#%%
# Output to pandas df and write to csv
df = pd.DataFrame(
        {"title" : titles[:-1],
         "founded" : founded,
         "aum" : aum,
         "manager" : manager,
         "strategies" : strategies})
df.to_excel('./businessinsider.xlsx')