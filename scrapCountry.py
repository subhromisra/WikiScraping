#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 14:24:09 2019

@author: subhro
"""

class ScrapCountry:
    countryUrl = 'https://www.britannica.com/topic/list-of-countries-1993160'
    
    def __init__(self):
        from bs4 import BeautifulSoup as bs
        import requests
        
        self.source = requests.get(ScrapCountry.countryUrl).content
        self.soup = bs(self.source,'lxml')
        
    def getCountryList(self):
        '''
        Scrap the names of all the available countires from britannica
        '''
        
        self.countryList = self.soup.find_all('li')
        country = []
        
        for c in self.countryList:
            if c.div != None:
                if c.div.text.strip() > '':
                    country.append(c.div.text.strip())

        return country
    
    def saveList(self,countryList):
        '''
        save the country list in a csv file
        '''
        import pandas as pd
        
        countryDict = {'Country':countryList}
        countryDf = pd.DataFrame(countryDict)
        
        countryDf.to_csv('Countries.csv',index = False)
        
        return