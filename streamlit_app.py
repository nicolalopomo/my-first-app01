import streamlit as st
import pandas as pd

import streamlit as st

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


st.title("MY WEB APPLICATION!")

st.text("Yeh, this is really my first app!",
        text_alignment="right")


data = st.slider("Select a specific value", 0, 30, 15)

st.write("The selected value is :", data)

st.header("I am a header!")

st.subheader("I am a subheader!")

st.write("I am a text!")

st.header("I am :green[green]")

st.write("I am **bold**")


st.write("My age is:", 48)

my_list = ["Python", "C++", "Java"]
st.write("My list is", my_list)

my_dict = {"First Lang":"Python", "Second Lang":"C++", "Third Lang":"Java"}
st.write("My dict is", my_dict)


my_new_dict = {"Item 1":[1, 2, 3], "Item 2":["A", "B", "C"]}
df = pd.DataFrame(my_new_dict)
st.write("This one is a data frame:", df)



my_sports = ["Soccer", "Tennis", "Basketball"]

# Button
if st.button("Sports", type="primary"):
    st.write(my_sports)


# Checkbox
check_out = st.checkbox("Do you like soccer?")

if check_out:
    st.write("Great!")
else:
    st.write("What a pity!")


# Radio button
fav_sport = st.radio("What is your favourite sport?", my_sports)

if fav_sport == "Soccer":
    st.write("Great!")
else:
    st.write("What a pity!")



# Selectbox
my_sports_tup = ("Soccer", "Tennis", "Basketball")
chk_selection = st.selectbox("Which sport?", my_sports_tup)

st.write("You like " + chk_selection)


# Multiselect
players_gol_dict = {"Ronaldo": "10", "Messi": "32", "Fonseca": "32"}
name_players = ["Ronaldo", "Messi", "Fonseca"]
select_players = st.multiselect("Select Players",name_players )

for player in select_players:
    st.write(f"{player} realized {players_gol_dict[player]} goals")


# Range slider
age_range = st.slider("Select the age range", 18, 99, (20, 40))
st.write("The range of age is:", age_range)


# Text input
my_name = st.text_input("Enter your name:", placeholder="They here your name...")
st.write("Your name is:", my_name)

# Numerical input
my_age = st.number_input("What is your age",
                         min_value=18, max_value=99, value=50, step=1)

st.write(f"Your age is {my_age}")


# Form
with st.form("Please fill the form"):
    
    my_name_form = st.text_input("Enter your name:", placeholder="They here your name...")
    my_age_form = st.number_input("What is your age",
                         min_value=18, max_value=99, value=50, step=1)
    
    submitted = st.form_submit_button()

if submitted:
    st.success(f"Your name is {my_name_form} and your age {my_age_form}")