import streamlit
s_list = ["search","music",'name','author','duration',]
def init():
    for element in s_list:
        if element not in streamlit.session_state:
            print(f"initialized {element}")
            streamlit.session_state[element] = 0
    if 'volume' not in streamlit.session_state:
        streamlit.session_state["volume"] = 50