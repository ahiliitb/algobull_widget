import streamlit as st

def main():
    # Define session state to store the input message
    if 'input_message' not in st.session_state:
        st.session_state['input_message'] = ''

    # Create a form
    form = st.form("my_form")
    input_text = form.text_input('Enter your message', value=st.session_state['input_message'], key="input_text_box")
    submitted = form.form_submit_button("Submit")

    if submitted:
        # Perform any desired actions with the submitted message
        st.write(f'Submitted message: {input_text}')
        st.session_state['input_message'] = ''  # Clear the input text box

    # Clear the input text box when the user manually clears the input
    if input_text == '':
        st.session_state['input_message'] = ''

    # Clear the input text box on the next re-render
    form.text_input('', key='clear_input', value='')

if __name__ == "__main__":
    main()