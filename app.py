#python file. 
import streamlit as st
import requests

st.title("PDF AI Assistant") #header name

#this is to upload the pdf file
#type 
uploaded_file = st.file_uploader(
    "Upload a PDF file",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success(f"File selected: {uploaded_file.name}")

    if st.button("Send PDF to n8n"):

        webhook_url = "https://abeersalman7979.app.n8n.cloud/webhook-test/pdf-agents"

        #this would be preparning the file. 
        #this one (application/pdf) would tell the n8n that this is the type pf the pdf. 
        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                "application/pdf"
            )
        }

        #post to send the data and get for gettining the data. 
        #here we decide where we can send the file 'webhook_url' 
        #here we save the response from n8n. 
        #if 200 (response.status_code) this sufffull 
        #if 400 (response.status_code) this filed ..etc
        response = requests.post(
            webhook_url,
            files=files
        )

        st.write("Status Code:", response.status_code)

        st.write("Response from n8n:") #this is the title from the user 'Response from n8n'

        #this is we use try becouse we are not sure that this would always give me a json that's why we say this is try. 
        #if it is not json it would replay with text. 
        try:
            st.json(response.json())
        except:
            st.write(response.text)
