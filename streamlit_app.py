import streamlit 

streamlit.title('My Parents New Healthy Driver')

streamlit.header('🥣 My Parents New Healthy Driver')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞 hard=Boiled Free-Range Egg')


streamlit.header('🍌🥭 Crie seu próprio smoothie de frutas 🥝🍇')
import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries']) 
frutas_to_show = my_fruit_list.loc[fruits_selected]


streamlit.dataframe(frutas_to_show)
