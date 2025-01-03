
import streamlit as st
import base64

st.write("HIUIII")

# Path to your PDF file (make sure the file exists and is accessible)
pdf_file_path = "resume.pdf"  # Replace with your PDF file path or URL

with open(pdf_file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></embed>'

st.markdown(pdf_display, unsafe_allow_html=True)