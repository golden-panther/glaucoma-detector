import streamlit as st
import tensorflow as tf
from tensorflow import keras
import cv2

def import_and_predict(image_data, model):
    	bgr_img = cv2.imread(image_data)
    	b,g,r = cv2.split(bgr_img)
    	rgb_img = cv2.merge([r,g,b])
    	new_array = cv2.resize(rgb_img, (100, 100))
    	x = new_array.reshape(-1, 100, 100, 3)
	x = x/255.0
	prediction = model.predict([x])
	return prediction

model = tf.keras.models.load_model('my_model2.h5')

st.write("""
         # Glaucoma detector
         """
         )

st.write("This is a simple image classification web app to predict glaucoma through fundus image of eye")

file = st.file_uploader("Please upload an image file", type=["jpg"])
#
if file is None:
    st.text("You haven't uploaded a jpg image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    prediction = import_and_predict(image, model)
    pred = prediction[0][0]
    if(pred>0.5):
  	print("Healthy")
    else:
  	print("Glaucomatous")