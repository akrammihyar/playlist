import pandas as pd
import streamlit as st

st.markdown("""# Date Night

Test test test).
""")

df = pd.read_csv("questions.csv")
decks = list(range(1,3))

decks_list = st.multiselect(label="Choose card Deck", options=decks, default= ['fun'])
                                                                               
selected_decks = st.multiselect(label="Choose card Deck", options=decks)

if st.button('Play'):
    if len(decks_list) == 1:
         for decks in selected_decks:
            id = df.loc[df['deck'] == decks, 'id']
            st.write(f"Id for {decks} is {id}")
    
    if df[df['name'] == playlist_name].shape[0] > 0:
        card = df[df['name'] == selected_decks].to_dict(orient='records')[0]
        
    else:
        st.write("Please select at least one deck.")
 
    if isinstance(card):
        link = f"### Your Spotify Playlist: [{card['name']}]({card['link']})"
        st.markdown(link, unsafe_allow_html=True)
    else:
        st.markdown(card)
