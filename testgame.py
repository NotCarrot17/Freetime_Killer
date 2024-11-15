import streamlit as st

st.subheader("Lets try on the code!")
st.divider()

# Displays the game if code for it has been generated
if "game_code" in st.session_state:
    # Render the game code directly in the Streamlit app
    st.components.v1.html(st.session_state.game_code, height=500, width=700)
else:
    st.write("Generate the game code in the 'Generation' tab to start playing.")