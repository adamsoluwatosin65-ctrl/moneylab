import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Quick Question", page_icon="🥺")

# 1. Success State Logic
if 'agreed' not in st.session_state:
    st.session_state.agreed = False

if st.session_state.agreed:
    st.balloons()
    st.success("I knew you were a legend! 🫡")
    st.markdown("### Account Details\n**OPAY**\n**8026294248**\n\n*Transfer received in advance!* 🤝")
    if st.button("Restart"):
        st.session_state.agreed = False
        st.rerun()
else:
    st.title("Quick Question")
    st.subheader("send me 2k? 🥺")

    # 2. The "Yes" Button (Standard Streamlit)
    if st.button("Yes", type="primary", use_container_width=True):
        st.session_state.agreed = True
        st.rerun()

    # 3. The "Running No" Button (JavaScript/HTML)
    # This creates a button that moves whenever "touchstart" or "mouseover" occurs
    html_code = """
    <div id="container" style="height: 300px; width: 100%; position: relative; border: 1px dashed #ccc; border-radius: 10px;">
        <button id="noButton" style="
            position: absolute; 
            top: 50%; 
            left: 50%; 
            transform: translate(-50%, -50%);
            padding: 10px 30px; 
            background-color: #ff4b4b; 
            color: white; 
            border: none; 
            border-radius: 5px; 
            cursor: pointer;
            transition: 0.1s;
            font-weight: bold;
        ">No</button>
    </div>

    <script>
        const btn = document.getElementById('noButton');
        const container = document.getElementById('container');

        function moveButton() {
            const containerWidth = container.offsetWidth - btn.offsetWidth;
            const containerHeight = container.offsetHeight - btn.offsetHeight;
            
            const randomX = Math.floor(Math.random() * containerWidth);
            const randomY = Math.floor(Math.random() * containerHeight);
            
            btn.style.left = randomX + 'px';
            btn.style.top = randomY + 'px';
            btn.style.transform = 'none';
        }

        // Trigger on both Mouse (PC) and Touch (Mobile)
        btn.addEventListener('mouseover', moveButton);
        btn.addEventListener('touchstart', (e) => {
            e.preventDefault(); // Prevents the actual click
            moveButton();
        });
    </script>
    """
    
    components.html(html_code, height=350)
