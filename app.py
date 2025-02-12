import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.header('Market of used cars.Original data')
st.write('Filter the data below to see the ads by manufacturer')

# Load data
df = pd.read_csv("vehicles_us.csv")

df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])
df['model'] = df['model'].apply(lambda x: ' '.join(x.split()[1:]))

df = df.rename(columns= {'price': 'Price (USD)', 
                         'model_year': 'Model Year', 
                         'model': 'Model', 
                         'condition': 'Condition', 
                         'cylinders': 'Cylinders', 
                         'fuel': 'Fuel', 
                         'odometer': 'Odometer', 
                         'transmission': 'Transmission', 
                         'type': 'Type', 
                         'paint_color': 'Paint Color', 
                         'is_4wd': '4WD', 
                         'date_posted': 'Date Posted', 
                         'days_listed': 'Days Listed', 
                         'manufacturer': 'Manufacturer'
                         })

df = df[['Price (USD)', 
         'Model Year',
         'Manufacturer',  
         'Model', 
         'Condition', 
         'Cylinders', 
         'Fuel', 
         'Odometer', 
         'Transmission', 
         'Type', 
         'Paint Color', 
         '4WD', 
         'Date Posted', 
         'Days Listed'
         ]]

df['Manufacturer'] = df['Manufacturer'].str.capitalize()
df['Model'] = df['Model'].str.capitalize()

def convert_to_uppercase(row, string): 
    if row == string: 
        return row.upper() 
    return row

string = 'Bmw' 
df['Manufacturer'] = df['Manufacturer'].apply(lambda x: convert_to_uppercase(x, string))

string = 'Gmc'
df['Manufacturer'] = df['Manufacturer'].apply(lambda x: convert_to_uppercase(x, string))

manufacturer_choice = df['Manufacturer'].unique()

selected_menu = st.selectbox('Select a manufacturer', manufacturer_choice)

min_year, max_year = int(df['Model Year'].min()), int(df['Model Year'].max())

year_range = st.slider("Year Range", 
                       value= (min_year, max_year), 
                       min_value= min_year, 
                       max_value= max_year
                       )

actual_range = list(range(year_range[0], year_range[1] + 1))

df_filtered = df[(df['Manufacturer'] == selected_menu) & (df['Model Year'].isin(list(actual_range)))]

df_filtered

st.header('Price Analysis')
st.write('[PH]')

list_for_hist = ['Model Year', 
                 'Manufacturer', 
                 'Condition', 
                 'Fuel', 
                 'Transmission', 
                 'Type']

selected_type = st.selectbox('Split for price distribution', list_for_hist)

fig1 = px.histogram(df, 
                    x= "Price (USD)", 
                    color= selected_type
                    )
fig1.update_layout(title= "<b> Split price by {} </b>".format(selected_type))
fig1.update_xaxes(range= [0, 100000])
st.plotly_chart(fig1)


# The age filter is a gradient instead of a discrete value toggle. Why?
def age_category(x): 
    if x < 5: 
        return '<5'
    elif x >= 5 and x < 10: 
        return '5-10'
    elif x >= 10 and x <20: 
        return '10-20'
    else: 
        return '>20'

 
df['Age'] = 2025 - df['Model Year']

df['Age Category'] = df['Age'].apply(age_category)

scatter_list = ['Odometer', 
                'Age', 
                'Days Listed'
                ]

scatter_menu = st.selectbox('Price dependency on', scatter_list)



fig2 = px.scatter(df, 
                  x= "Price (USD)", 
                  y= scatter_menu, 
                  color= 'Age Category', 
                  hover_data= ['Model Year']
                  )
fig2.update_layout(title= "{} </b>".format(selected_type))
st.plotly_chart(fig2)


fig3 = px.parallel_coordinates(df, 
                               color= 'Price (USD)') 
fig3.update_layout(width= 1500, 
                   height= 600)
st.plotly_chart(fig3)


fig4 = px.strip(df, 
                x= "Price (USD)", 
                y= "Manufacturer" 
)
                
st.plotly_chart(fig4)