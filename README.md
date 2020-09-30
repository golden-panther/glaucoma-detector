# glaucoma-detector
Always remember that tensorflow does not support python 3.8. It supports upto version 3.7 only.

## Install all the required packages from requirements.txt

To run our glaucoma detector on your machine by cloning
* Type "streamlit run glaucoma_app.py" in your terminal or cmd
* The web app opens up in a local host

or use our ngrok instance created in google colab.......http://7431ba80922e.ngrok.io/ (will not always work)

* I provided two folders Glaucomatous and Healthy. These contain images from my test set. Use them for testing our project.

Then upload a (jpg) cropped fundus image of eye(if not cropped, see note). Our model predicts whether affected by glaucoma or not.

Note: The image should be cropped around the optic nerve part.(see the 'full to cropped' for reference)
