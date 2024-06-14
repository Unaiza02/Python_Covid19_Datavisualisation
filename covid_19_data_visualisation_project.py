# -*- coding: utf-8 -*-
"""Covid 19 Data visualisation Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vepkiIAFsKJB0n2OS1WS7UbHnObiVMsG
"""

import pandas as pd
import numpy as np
from google.colab import files
uploaded=files.upload()
import pandas as pd
data=pd.read_csv('Book1.csv')
avg=data.groupby('Name')['Grade'].mean()
print(avg)
data.groupby('Subject')['Grade'].mean().plot(kind='bar')
data['Grade_Square']=np.square(data['Grade'])

import pandas as pd
import numpy as np
from google.colab import files
uploaded=files.upload()
import pandas as pd
data=pd.read_csv('Book2.csv')
sum=data.groupby('Product')['Sales'].sum()
print(sum)
data.groupby('Product')['Sales'].sum().plot(kind='line')
data['Log_Sales']=np.log(data['Sales'])

import pandas as pd

df = pd.read_csv('Book3.csv', header=1)

display(df)

import plotly.express as px
import pandas as pd
import csv
from google.colab import files


uploaded = files.upload()

x = []
y = []
z = []


with open('Book3.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(plots)
    for row in plots:
        x.append(row[3])
        y.append(row[2])
        z.append(row[1])


df = pd.DataFrame({'Cases': x, 'Years': y, 'Countries': z})





year_order = sorted(df['Years'].unique())

fig = px.bar(df, x='Cases', y='Years', color='Countries',
             labels={'Cases': 'Cases', 'Years': 'Years', 'Countries': 'Countries'},
             title='Covid cases and deaths overtime',
             hover_name=z)
fig.update_yaxes(categoryorder='array', categoryarray=year_order)




fig.show()

import plotly.express as px
import pandas as pd
import csv

with open('Book3.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')


    next(plots)


    countries = []
    total_cases = []


    for row in plots:
        country = row[1]
        cases = int(row[2]) if row[2].isdigit() else 0
        deaths = int(row[3]) if row[3].isdigit() else 0
        total_cases.append(cases + deaths)
        countries.append(country)


top_two_indices = sorted(range(len(total_cases)), key=lambda i: total_cases[i], reverse=True)[:2]


top_countries = [countries[i] for i in top_two_indices]
top_cases = [total_cases[i] for i in top_two_indices]


df = pd.DataFrame({'Countries': top_countries, 'TotalCases': top_cases})






fig = px.scatter(df, x='Countries', y='TotalCases', title='Top Two Countries with Maximum Total Cases',
                 hover_name='Countries', hover_data={'TotalCases': True})
fig.update_layout(xaxis_title='Countries', yaxis_title='Total Cases', showlegend=False)



fig.show()