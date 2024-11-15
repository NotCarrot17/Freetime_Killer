import streamlit as st

st.markdown("<h4 style='text-align: center; color: white; padding: 50px'> Are you bored? Wanna play a game? 😈 </h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: white; padding: 1px'> <i> Introducing </i> </h4>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white; padding-top: 1px'> Freetime Killer </h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: white; padding-bottom: 100px'> An AI powered web app </h6>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: left; color: white;'> 👉  Use AI to generate everything for you! </h4>", unsafe_allow_html=True)

if 'character_button' not in st.session_state:
    st.session_state.character_button = False
if 'game_button' not in st.session_state:
    st.session_state.game_button = False
if 'music_button' not in st.session_state:
    st.session_state.music_button = False
    
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("need a character design?")
    with col2:
        if st.button("yes!"):
            st.session_state.character_button = True
    if st.session_state.character_button:
        st.write("∘ ∘ ∘ ( °ヮ° ) ! im alive!") 
        st.divider()
    
with st.container():
    col1, col2 = st.columns([0.4, 0.6])
    with col1:
        st.subheader("how about a game?")
    with col2:
        if st.button("yes!!"):
            st.session_state.game_button = True          
    if st.session_state.game_button:
        st.write("this shooter for example")
        st.write("( -_•)▄︻テحكـ━一💥")
        st.write("pew pew")
        st.divider()

with st.container():
    col1, col2 = st.columns([0.6, 0.4])
    with col1:
        st.subheader("how about music to go with it?")
    with col2:
        if st.button("yes!!!!"):
            st.session_state.music_button = True          
    if st.session_state.music_button:
        st.write("♪┏(・o･)┛♪")
    st.divider()

