from PIL import Image
import streamlit as st
import subprocess


uploaded_file = st.file_uploader("Upload a file", type=["jpg", "jpeg", "png"])


# Call the other Python script and capture its output
output = subprocess.check_output(["python", "M_Imam_Project3.ipynb"]).decode("utf-8")

# Display the output in Streamlit
st.write("Output from other_script.py:")
st.write(output)

image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)







