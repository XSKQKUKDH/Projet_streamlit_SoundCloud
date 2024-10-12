import streamlit
s_list = ["search","music"]
def init():
    for element in s_list:
        if element not in streamlit.session_state:
            print(f"initialized {element}")
            streamlit.session_state[element] = None