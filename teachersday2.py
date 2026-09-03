import streamlit as st

st.markdown("<h1 style='text-align: center; color: #D63384;'>🌸 Happy Teacher's Day! 🌸</h1>", unsafe_allow_html=True)
st.markdown("<style>.stApp {background-color: #F4C2C2;}</style>", unsafe_allow_html=True) 
/* 3. Soft white text input box with a matching border */
    ''' 
    [data-testid="stTextInputRootElement"] {
        background-color: #FAFAFA !important; 
        border: 1.5px solid #8A646A !important;  
        border-radius: 8px;                    
    }
    '''


name = st.text_input("Enter your name:")

if st.button("💌 Open 💌"):
    name_clean = name.strip()
    name_lower = name_clean.lower()

    if name_lower == "sonia":
        message = "Thank you for always making us feel comfortable in your class and for being someone we can talk to. Your classes have given us many good memories, and we really appreciate you 🌸️"
    elif name_lower == "lekha":
        message = "We really appreciate all the patience, effort, and time you put into helping us. Your classes are always nice 💖"
    elif name_lower == "jyothi":
        message = "Thank you for everything you’ve taught us and for making our time in your class so much better ⭐️"
    elif name_lower == "vandana":
        message = "We're very grateful for all the little things you do that make such a difference 🌈️"
    elif name_lower == "niharika":
        message = "Thank you for making even the most boring topics interesting and for always keeping the class fun and engaging 🌱"
    else:
        message = "You're not a teacher, what are you doing? 👽"

    st.markdown(f"**Dear {name_clean} Ma'am,**\n\n{message}\n\n🌷 Thank You! 🌷")

st.markdown("<div style='text-align: center; font-size: 18px; margin-top: 50px;'>🌷  💕  🌸  ⭐  🌸  💕  🌷</div>", unsafe_allow_html=True)
