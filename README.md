# Glaucoma detector [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/golden-panther/glaucoma-detector/glaucoma_app.py)

Link: https://share.streamlit.io/golden-panther/glaucoma-detector/glaucoma_app.py

(If app at above link doesn't work then use this project by downloading and running it on your local PC)

## Web Page
![alt text](https://github.com/golden-panther/glaucoma-detector/blob/master/lit.jpg)

## Healthy Eye
![alt text](https://github.com/golden-panther/glaucoma-detector/blob/master/healthy%20lit.jpg)

## Glaucomatous Eye
![alt text](https://github.com/golden-panther/glaucoma-detector/blob/master/glaucoma%20lit.jpg)

# >> Details
## Part 1
* We have collected all the publicly available labelled(glaucoma or normal) fundus images of eye from web.
* Some are already cropped and some are full. So, we cropped the full fundus images too. 
* We bulk renamed all the images in the two classes using https://www.bulkrenameutility.co.uk/
* Then we bulk converted all the images to jpg using https://www.xnview.com/en/xnconvert/
* Number of images in both classes are not equal. They are highly imbalanced. Then we balanced by removing extra images.
* Finally, we sticked with 1,115 images of each class totalling 2,230 (Contact me if you want this data). And we divided them randomly into train, val and test sets in the ratio 8:1:1 using https://pypi.org/project/split-folders/
## Part 2
* We uploaded all these images to my google drive and trained on various CNN architectures from simple to advanced.
* We did augmentation of data using keras ImageGenerator to cut down high variance. But there is some bias due to low and bad data.
* We used keras (2.4.3) and tesorflow (2.3.0) on top of python (3.6.9). (You can see the code in train.py)
* We trained on train set and validated on validation set after each epoch. Finally tested the test set.
* It gave 93 percent AUC score, some good accuracy, precision and recall values. We saved the model file(h5) for further usage.
* Then we built a simple streamlit app for hosting on web.


# >> Usage: 

Always remember that tensorflow does not support python 3.8. It supports upto version 3.7 only.

To use our project - go to this link https://share.streamlit.io/golden-panther/glaucoma-detector/glaucoma_app.py

(or)

To run this app

```
pip install -r requirements.txt
streamlit run https://raw.githubusercontent.com/golden-panther/glaucoma-detector/master/glaucoma_app.py
```

(or)

To run our glaucoma detector on your machine by cloning this repository,
* Type the following in your terminal or cmd:
```
pip install -r requirements.txt
streamlit run glaucoma_app.py
```
* The web app opens up in a local host. Then you can use it for classifying. That's it!

* Upload a (jpg) cropped fundus image of eye(if not cropped, see note). Our model predicts whether affected by glaucoma or not.
* I provided two folders Glaucomatous and Healthy. These contain images from my test set. Use these if you don't have any fundus images with you.

Note: The image should be cropped around the optic nerve part.(see the below **full to cropped** image for reference)

![alt text](https://github.com/golden-panther/glaucoma-detector/blob/master/full%20to%20cropped.jpg)
