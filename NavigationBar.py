import streamlit as st

st.title(":red[_Freetime Killer_]")

# Display a title at the top in red

# Navigation setup with Streamlit's `st.Page`
pages = {
    "Who are we?": [
        st.Page("Intro.py", title="Introduction"),
    ],
    "God Mode: ON.": [
        st.Page("Generator.py", title="Generator"),
    ],
    "Now, Lets play the game!": [
        st.Page("testgame.py", title="Gaming Mode: ON")
    ],
    "Want the previous saved games? We gotchu": [
        st.Page("Library.py", title="Library"),
    ],
}

# Initialize the navigation component
pg = st.navigation(pages)
pg.run()
