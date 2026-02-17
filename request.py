import streamlit as st
import random

st.set_page_config(page_title="Quick Question", page_icon="🥺")

# Initialize position in session state so it stays put until clicked
if 'no_pos' not in st.session_state:
    st.session_state.no_pos = 1
if 'agreed' not in st.session_state:
    st.session_state.agreed = False

st.title("Quick Question")

if not st.session_state.agreed:
    st.subheader("send me 2k? 🥺")
    
    # Create 4 columns to give the "No" button room to jump around
    cols = st.columns(4)
    
    # The "Yes" button stays put in column 0
    with cols[0]:
        if st.button("Yes", type="primary"):
            st.session_state.agreed = True
            st.rerun()
            
    # The "No" button jumps to a random column (1, 2, or 3) when clicked
    with cols[st.session_state.no_pos]:
        if st.button("No"):
            # Change the position for the next render
            st.session_state.no_pos = random.randint(1, 3)
            st.toast("Too slow! 😂")
            st.rerun()

else:
    st.balloons()
    st.success("I knew you were a legend! 🫡")
    st.markdown("""
    ### Account Details
    **Bank:** OPAY  
    **Account:** 8026294248  
    *Transfer received in advance!* 🤝
    """)
    if st.button("Start Over"):
        st.session_state.agreed = False
        st.rerun()
