import streamlit as st

st.set_page_config(page_title="Home")
if 'role' not in st.session_state:
    st.session_state['role'] = None

def home():
    col = st.columns(1)[0]
    with col:
        if st.button("FinLama", type="primary", use_container_width=True):
            st.session_state['role'] = 'finlamma'
            st.rerun()
        if st.button("FinLava", type="secondary",use_container_width=True):
            st.session_state['role'] = 'finlava'
            st.rerun()

def logout():
    st.write("going to home page...")
    st.session_state['role'] = None
    st.rerun()


if st.session_state['role']:
    role = st.session_state['role']

    home_page = st.Page(logout, title="Log out", icon=":material/home:")
    if role == "finlamma":
        finlamma = st.Page("./finlamma.py", title="In FinLamma model")
        pg = st.navigation([finlamma,home_page])
    elif role == "finlava":
        finlava = st.Page("./finlava.py", title="In FinLava model")
        pg = st.navigation([finlava,home_page]) 
    pg.run()
else:
    pg = st.navigation([st.Page(home)])
    pg.run()