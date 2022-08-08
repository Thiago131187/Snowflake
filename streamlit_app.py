import streamlit 

streamlit.title('My Parents New Healthy Driver')

streamlit.header('🥣 My Parents New Healthy Driver')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞 hard=Boiled Free-Range Egg')


streamlit.header('🍌🥭 Crie seu próprio smoothie de frutas 🥝🍇')
import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
