import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

st.set_option('deprecation.showfileUploaderEncoding', False)

# @st.cache(suppress_st_warning=True,allow_output_mutation=True)
def import_and_predict(image_data, model):
    image = ImageOps.fit(image_data, (100,100),Image.ANTIALIAS)
    image = image.convert('RGB')
    image = np.asarray(image)
    st.image(image, channels='RGB')
    image = (image.astype(np.float32) / 255.0)
    img_reshape = image[np.newaxis,...]
    prediction = model.predict(img_reshape)
    return prediction

model = tf.keras.models.load_model('my_model2.h5')

st.write("""
         # ***Glaucoma detector***
         """
         )

st.write("This is a simple image classification web app to predict glaucoma through fundus image of eye")

file = st.file_uploader("Please upload an image(jpg) file", type=["jpg"])

if file is None:
    st.text("You haven't uploaded a jpg image file")
else:
    imageI = Image.open(file)
    prediction = import_and_predict(imageI, model)
    pred = prediction[0][0]
    if(pred > 0.5):
        st.write("""
                 ## **Prediction:** You eye is Healthy. Great!!
                 """
                 )
        st.balloons()
    else:
        st.write("""
                 ## **Prediction:** You are affected by Glaucoma. Please consult an ophthalmologist as soon as possible.
                 """
                 )
