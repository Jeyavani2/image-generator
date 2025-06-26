#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
st.title('image generator')
pr=st.text_input("enter pr")
if pr is not None and st.button("generate"):
    client=genai.Client(api_key='AIzaSyDdDYoT8dGRfNpXRUAHrQMHHXUPOu-Hhpk')
    st.write('not ok')
    response=client.models.generate_images(
        model='imagen-3.0-generate-002',
        prompt=pr,
        config=types.GenerateImagesConfig(number_of_images=4
                                         )
    )
    for generated_image in response.generated_images:
        image=Image.open(BytesIO(generated_image.image.image_bytes))
        st.image(image)

