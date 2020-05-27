#!/usr/bin/env python
# coding: utf-8

# In[13]:


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 12:23:01 2020

@author: nabeelhussain
"""

# storing and anaysis
import numpy as np
import pandas as pd

# visualization
import plotly.express as px

# hide warnings
import warnings
warnings.filterwarnings('ignore')

# importing datasets
data = pd.read_csv('/Users/nabeelhussain/Desktop/NEU/EECE5642/covid_19_clean_complete.csv',parse_dates=['Date'])
data.head()

# replacing Mainland china with just China
data['Name'] = data['Name'].replace('Mainland China', 'China')

data = data.groupby(['Date', 'Name'])['Confirmed', 'Deaths', 'Recovered'].max()
data = data.reset_index()
data['Date'] = pd.to_datetime(data['Date'])
data['Date'] = data['Date'].dt.strftime('%m/%d/%Y')
data['size'] = data['Confirmed'].pow(0.3)


fig = px.scatter_geo(data, locations="Name", locationmode='country names',color="Confirmed", size='size', hover_name="Name", 
                     range_color= [0, max(data['Confirmed'])+2],projection="natural earth", animation_frame="Date", 
                     title='Number of cases over time')
fig.update(layout_coloraxis_showscale=True)
fig.show()

fig2 = px.scatter_geo(data, locations="Name", locationmode='country names',color="Deaths", size='size', hover_name="Name", 
                     range_color= [0, max(data['Deaths'])+2],projection="natural earth", animation_frame="Date", 
                     title='Number of Deaths over time')
fig2.update(layout_coloraxis_showscale=True)
fig2.show()

fig3 = px.scatter_geo(data, locations="Name", locationmode='country names',color="Recovered", size='size', hover_name="Name", 
                     range_color= [0, max(data['Recovered'])+2],projection="natural earth", animation_frame="Date", 
                     title='Number of Recovered over time')
fig3.update(layout_coloraxis_showscale=True)
fig3.show()


# In[9]:





# In[10]:





# In[ ]:




