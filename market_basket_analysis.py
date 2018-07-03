#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 11:20:17 2018

@author: eduardo

https://datafai.com/2017/11/15/market-basket-analysis-or-association-rules-or-affinity-analysis-or-apriori-algorithm/
"""

print 'Market Basket Analysis or Association Rules or Affinity Analysis or Apriori Algorithm'

print
print 'Example 1'


import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

df = pd.read_csv('data/Retail_Data.csv')
print df.shape
print df.head()
print df.tail()

df = df.iloc[:,1:]
print df.head()

df1 = pd.get_dummies(df)
print df1.head()

print df1.shape

# find rules wich have at least 5% of support level
frequent_items = apriori(df1, min_support=0.05, use_colnames = True)

# Build rules with minimum lift of 1
rules = association_rules(frequent_items, metric='lift',min_threshold=1)
print type(rules)
print rules.shape
print rules

print 'Top 10 rules with highest support'
print rules.sort_values('support', ascending=False).head(10)

print 'Top 10 rules with highest confidence'
print rules.sort_values('confidence', ascending=False).head(10)

print 'Top 10 rules with highest lift'
print rules.sort_values('lift', ascending=False).head(10)

# Selecting only the rules with lift > 2, confidence < 0.6, and support > 0.2
print rules[(rules['lift'] >= 2)
            & (rules['confidence'] >= 0.6)
            & (rules['support'] >= 0.2)]