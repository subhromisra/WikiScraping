#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 15:56:55 2019

@author: subhro
"""

from scrapCountry import ScrapCountry
import wikiScrap
import pandas as pd
import datetime
#import numpy as np
#import matplotlib.pyplot as plt

start = datetime.datetime.now()
cl = ScrapCountry()
cl.saveList(cl.getCountryList())

df = pd.read_csv('Countries.csv')

iList = []
pList = []
gList = []
hList = []
cList = []

for country in df['Country']:
    obj = wikiScrap.WebScrap(country)
    
    iList.append(obj.perCapitaIncome())
    pList.append(obj.population())
    gList.append(obj.giniCoefficient())
    hList.append(obj.humanDevIndex())
    cList.append(country)
    
    del obj
    
worldDevInfo = pd.DataFrame({'Country':cList,
                             'Per Capita Income':iList,
                             'Population':pList,
                             'Gini Coefficient':gList,
                             'Human Development Index':hList})
    
worldDevInfo.to_csv('World_Development_Info.csv',index = False)
end = datetime.datetime.now()

print('Total time taken: ',(end - start))
    