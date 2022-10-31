# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 11:16:17 2022

@author: ds22abr

week 3 prectical 1 {a}

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
barc = pd.read_csv('BCS_ann.csv')
print("\n Barclays Fail: \n", barc)

print("-----------------------------------------------------------------------")

bp = pd.read_csv ('BP_ann.csv')
print("\n BP Fail: \n", bp)

print("-----------------------------------------------------------------------")

tsco = pd.read_csv ('TSCO_ann.csv')
print("\n Tsco Fail: \n", tsco)

print("-----------------------------------------------------------------------")

vod = pd.read_csv ('VOD_ann.csv')
print("\n Vod Fail: \n", vod)

print("-----------------------------------------------------------------------")

a = barc['ann_return'].values
print(a)

b = bp['ann_return'].values
print(b)

c = tsco['ann_return'].values
print(c)

d = vod['ann_return'].values
print(d)

data = [a,b,c,d]

plt.figure()
plt.subplots_adjust(hspace=0.4, wspace= 0.4)
for i in range(4):
    plt.subplot(2,2, i+1)
    plt.hist(data[i], bins=5)
    
plt.legend()
plt.show()



   
"""
week 3 prectical 1 {b}

"""

plt.figure()
plt.hist(a, alpha=0.7, bins=4, label=("Barclays"))
plt.hist(b, alpha=0.6, bins=4, label=("BP"))
plt.legend()
plt.show()



"""

week 3 prectical 1 {c}

"""


plt.Figure()
plt.boxplot([a,b,c,d], labels=("Barclays","BP","TSCO","VOD"))
plt.ylabel("N")
plt.show()




"""

week 3 prectical 1 {d}

"""


plt.Figure()
fig, ax = plt.subplots(1,1)
plt.violinplot([a,b,c,d], showmedians=True)
ax.set_xticks([1,2,3,4])               
ax.set_xticklabels(["Barclays","BP","TSCO","VOD"])
plt.ylabel("N")
plt.show()



"""
week 3 prectical 2 [a]

"""

market = np.array([33367,68785,20979,29741])
companies=["Barclays","BP", "TESCO", "Vodaphone"]

plt.figure()
plt.pie(market, labels=companies)
plt.show()


"""
week 3 prectical 2 [b]

"""

ftse = 1840000
market = market/ftse

plt.Figure()
plt.pie(market, labels=companies, normalize=False)
plt.show()


   
   