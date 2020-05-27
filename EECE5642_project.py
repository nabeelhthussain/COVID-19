#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:58:15 2020

@author: nabeelhussain
"""

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
import plotly

# importing datasets
data = pd.read_csv('/Users/nabeelhussain/Desktop/NEU/EECE5642/time_series_covid19_confirmed_global.csv')

usa = data.iloc[225,4:len(data)]

plotly.plot(list(range(0,82)), usa)
