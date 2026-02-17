import streamlit as st

st.title("Quick Question")

# Use session state to track if they said yes
if 'agreed' not in st.session_state:
    st.session_state.agreed = False

if not st.session_state.agreed:
    st.subheader("send me 2k? 🥺")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Yes"):
            st.session_state.agreed = True
            st.rerun()
            
    with col2:
        # In web apps, we can't easily make buttons "run away" 
        # but we can make them do nothing or show a funny message!
        if st.button("No"):
            st.warning("Error: Button not found. Please try the green one. 😉")

else:
    st.balloons()
    st.success("I knew you were a legend! 🫡")
    st.info("OPAY: 8026294248 \n\n Transfer received in advance! 🤝")
