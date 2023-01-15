import pandas as pd
import streamlit as st

st.markdown("""# Date Night
Test test test ).
""")

df = pd.read_csv("questions.csv")
decks = ['fun', 'date', 'truth']

decks_list = st.multiselect(label="Choose card Deck", options=decks, default= ['fun'])
                                                                               
selected_decks = st.multiselect(label="Select people", options=people)

if st.button('Play'):
    if len(decks_list) == 1:
         for decks in selected_decks:
            id = df.loc[df['deck'] == decks, 'id']
            st.write(f"Id for {decks} is {id}")
    else:
        st.write("Please select at least one deck.")
