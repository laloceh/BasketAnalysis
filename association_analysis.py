#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 16:38:40 2018

@author: eduardo

http://pbpython.com/market-basket-analysis.html
"""

import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

df = pd.read_excel('data/OnlineRetail.xlsx')
print df.head()

# Cleaning the data
df['Description'] = df['Description'].str.strip()
df.dropna(axis=0, subset=['InvoiceNo'], inplace=True)
df['InvoiceNo'] = df['InvoiceNo'].astype('str')
df = df[~df['InvoiceNo'].str.contains('C')]
        
# To consolidate the items into 1 
# transaction per row with each product 1 hot encoded. 

# France only
basket = (df[df['Country'] =="France"]
         .groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('InvoiceNo'))


print basket.head()

def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

basket_sets = basket.applymap(encode_units)
basket_sets.drop('POSTAGE', inplace=True, axis=1)

print basket_sets.head()

frequent_itemsets = apriori(basket_sets, min_support=0.07, use_colnames=True)

# generate the rules with their corresponding support, confidence and lift:
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules.head()
rules.tail(3)


# DONE!


#####################
# Analysis

rules[ (rules['lift'] >= 6) & (rules['confidence'] >= 0.8) ]

basket['ALARM CLOCK BAKELIKE GREEN'].sum()
#340.0

basket['ALARM CLOCK BAKELIKE RED'].sum()
#316.0
       
# is also interesting is to see how the combinations vary by country of 
# purchase. Let’s check out what some popular combinations might be in Germany:

basket2 = (df[df['Country'] =="Germany"]
          .groupby(['InvoiceNo', 'Description'])['Quantity']
          .sum().unstack().reset_index().fillna(0)
          .set_index('InvoiceNo'))

basket_sets2 = basket2.applymap(encode_units)
basket_sets2.drop('POSTAGE', inplace=True, axis=1)
frequent_itemsets2 = apriori(basket_sets2, min_support=0.05, use_colnames=True)
rules2 = association_rules(frequent_itemsets2, metric="lift", min_threshold=1)

rules2[ (rules2['lift'] >= 4) & (rules2['confidence'] >= 0.5)]  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    