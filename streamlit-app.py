import streamlit;
import pandas;

streamlit.title('My parents New Healthy Diner');

streamlit.header('Breakfast Menu');
streamlit.text('Pancakes');
streamlit.text('Muesli yogurt and blueberries');
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit');

selected_fruits = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index), ['Avocado', 'Strawberries']);

show_fruits = my_fruit_list.loc(selected_fruits)
streamlit.dataframe(show_fruits)
