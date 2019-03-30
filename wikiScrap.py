#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 23:32:02 2019

@author: subhro
"""
class WebScrap:
    
    wikiUrl = 'https://en.wikipedia.org/wiki/'
    
    def __init__(self,country):
        from bs4 import BeautifulSoup as bs
        import requests
        
        self.myUrl = WebScrap.wikiUrl + country
        self.source = requests.get(self.myUrl).content
        self.soup = bs(self.source,'lxml')
              
    def perCapitaIncome(self):
        ''' 
        scraps the per capita income(nominal) of the country from wikipedia
        '''
        import numpy as np
        import re
        
        self.incomeRec = self.soup.find_all('tr',class_ = 'mergedbottomrow')
        nPerCapita = ''
        
        for i in self.incomeRec:
            if 'per capita' in str(i).lower():
                nPerCapita = i.td.text.split('$')[1].replace('[',' ').replace(',','')
             
        try:        
            if nPerCapita > '':
                return float(re.findall('\d+',nPerCapita)[0])
            else:
                return np.NaN
        except ValueError:
            print('URL: ',self.myUrl)
            print('Error1 in Per capita Income: ',nPerCapita)
        except IndexError:
            print('URL: ',self.myUrl)
            print('Error2 in Per capita Income: ',nPerCapita)
        
    def population(self):
        ''' 
        scraps the latest available population of the country from wikipedia
        '''
        import numpy as np
        
        self.P = self.soup.find_all('tr',class_ = 'mergedrow')
        
        cont = True
        pop = ''
        for p in self.P:
            if 'population' in str(p).lower() and cont:
                pop = p.td.text.replace('[',' ').replace('(',' ')
                cont = False
        
        try:
            if pop > '':
                return int(pop.split()[0].replace(',',''))
                #return int(re.findall('\d+\,\d+\,\d+\,\d+',pop)[0])
            else:
                return np.NaN
        except ValueError:
            print('URL: ',self.myUrl)
            print('Error1 in Population: ',pop)
        except IndexError:
            print('URL: ',self.myUrl)
            print('Error2 in Population: ',pop)
        
    def giniCoefficient(self):
        ''' 
        scraps the Gini Coefficient of the country from wikipedia
        '''
        import numpy as np
        import re
        
        self.G = self.soup.find_all('tr')
        
        gini = ''
        cont = True
        for g in self.G:
            if 'gini coefficient' in str(g).lower() and cont:
                gini = g.td.text
                cont = False
                
        try:
            if gini > '':
                return float(re.findall('\d+\.\d+',gini)[0])
            else:
                return np.NaN
        except ValueError:
            print('URL: ',self.myUrl)
            print('Error1 in Gini: ',gini)
        except IndexError:
            return float(re.findall('\d+',gini)[0])
            
    def humanDevIndex(self):
        '''
        scraps the HDI of the country from wikipedia
        '''
        import numpy as np
        import re
        
        self.HDI = self.soup.find_all('tr')
        
        hdi = ''
        cont = True
        for h in self.HDI:
            if 'human development index' in str(h).lower() and cont:
                hdi = h.td.text
                cont = False
                
        try:
            if hdi > '':
                return float(re.findall('\d+\.\d+',hdi)[0])
            else:
                return np.NaN
        except ValueError:
            print('URL: ',self.myUrl)
            print('Error1 in HDI: ',hdi)
        except IndexError:
            return np.NaN