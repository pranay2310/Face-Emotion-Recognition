# Face-Emotion-Recognition
## Live Class Monitoring System(Face Emotion Recognition)
## Introduction
Emotion recognition is the process of identifying human emotion. People vary widely in their accuracy at recognizing the emotions of others. Use of technology to help people with emotion recognition is a relatively nascent research area. Generally, the technology works best if it uses multiple modalities in context. To date, the most work has been conducted on automating the recognition of facial expressions from video, spoken expressions from audio, written expressions from text, and physiology as measured by wearables.

Facial expressions are a form of nonverbal communication. Various studies have been done for the classification of these facial expressions. There is strong evidence for the universal facial expressions of seven emotions which include: neutral happy, sadness, anger, disgust, fear, and surprise. So it is very important to detect these emotions on the face as it has wide applications in the field of Computer Vision and Artificial Intelligence. These fields are researching on the facial emotions to get the sentiments of the humans automatically.
## Problem Statement
The Indian education landscape has been undergoing rapid changes for the past 10 years owing to the advancement of web-based learning services, specifically, eLearning platforms.

Global E-learning is estimated to witness an 8X over the next 5 years to reach USD 2B in 2021. India is expected to grow with a CAGR of 44% crossing the 10M users mark in 2021. Although the market is growing on a rapid scale, there are major challenges associated with digital learning when compared with brick and mortar classrooms. One of many challenges is how to ensure quality learning for students. Digital platforms might overpower physical classrooms in terms of content quality but when it comes to understanding whether students are able to grasp the content in a live class scenario is yet an open-end challenge. In a physical classroom during a lecturing teacher can see the faces and assess the emotion of the class and tune their lecture accordingly, whether he is going fast or slow. He can identify students who need special attention.

Digital classrooms are conducted via video telephony software program (ex-Zoom) where it’s not possible for medium scale class (25-50) to see all students and access the mood. Because of this drawback, students are not focusing on content due to lack of surveillance.

While digital platforms have limitations in terms of physical surveillance but it comes with the power of data and machines which can work for you. It provides data in the form of video, audio, and texts which can be analyzed using deep learning algorithms.

Deep learning backed system not only solves the surveillance issue, but it also removes the human bias from the system, and all information is no longer in the teacher’s brain rather translated in numbers that can be analyzed and tracked.

I will solve the above-mentioned challenge by applying deep learning algorithms to live video data. The solution to this problem is by recognizing facial emotions.
## Dataset Information
I have built a deep learning model which detects the real time emotions of students through a webcam so that teachers can understand if students are able to grasp the topic according to students' expressions or emotions and then deploy the model. The model is trained on the FER-2013 dataset .This dataset consists of 35887 grayscale, 48x48 sized face images with seven emotions - angry, disgusted, fearful, happy, neutral, sad and surprised. Here is the dataset link:- 
## Dependencies
Python 3

Tensorflow

Streamlit

Streamlit-Webrtc

OpenCV

## Model Creation
### 1) Using Sequential Model
Everything in life depends on time and therefore, represents a sequence. To perform machine learning with sequential data (text, speech, video, etc.) we could use a regular neural network and feed it the entire sequence, but the input size of our data would be fixed, which is quite limiting. Other problems with this approach occur if important events in a sequence lie just outside of the input window. What we need is (1) a network to which we can feed sequences of arbitrary length one element of the sequence per time step (for example a video is just a sequence of images; we feed the network one image at a time); and (2) a network which has some kind of memory to remember important events which happened many time steps in the past. These problems and requirements have led to a variety of different recurrent neural networks.
### Loss Acuracy Plot using Sequential
![3](https://user-images.githubusercontent.com/92773034/171333314-0b89963d-c418-46a4-87b7-8a9ed313b075.png)

### 2) Using Deep CNN
Deep convolutional neural network has recently been applied to image classification with large image datasets. A deep CNN is able to learn basic filters automatically and combine them hierarchically to enable the description of latent concepts for pattern recognition. However, many deep CNNs have the problems of overfitting and huge processing time In deep learning, a convolutional neural network (CNN, or ConvNet) is a class of artificial neural network, most commonly applied to analyze visual imagery.[1] They are also known as shift invariant or space invariant artificial neural networks (SIANN), based on the shared-weight architecture of the convolution kernels or filters that slide along input features and provide translation equivariant responses known as feature maps.[2][3] Counter-intuitively, most convolutional neural networks are only equivariant, as opposed to invariant, to translation.[4] They have applications in image and video recognition, recommender systems,[5] image classification, image segmentation, medical image analysis, natural language processing,[6] brain-computer interfaces,[7] and financial time series.[8]

CNNs are regularized versions of multilayer perceptrons. Multilayer perceptrons usually mean fully connected networks, that is, each neuron in one layer is connected to all neurons in the next layer. The "full connectivity" of these networks make them prone to overfitting data. Typical ways of regularization, or preventing overfitting, include: penalizing parameters during training (such as weight decay) or trimming connectivity (skipped connections, dropout, etc.) CNNs take a different approach towards regularization: they take advantage of the hierarchical pattern in data and assemble patterns of increasing complexity using smaller and simpler patterns embossed in their filters. Therefore, on a scale of connectivity and complexity, CNNs are on the lower extreme.

• The training gave the accuracy of 72.68% and test accuracy of 66.48%. It seems excellent. So, I save the model and the detection i got from live video was excellent.

• One drawback of the system is the some Disgust faces are showing Neutral .Because less no. of disgust faces are given to train .This may be the reason.

• I thought it was a good score should improve the score.

• Thus I decided that I will deploy the model.
### Loss & Accuracy Plot using DCNN
![4](https://user-images.githubusercontent.com/92773034/171333792-071b3006-9fbf-4ad8-baa2-a0ec6733b59e.png)
To See the Training and Testing python file follow this link:
## Realtime Local Video Face Detection
I created one patterns for detecting and predicting single faces and as well as multiple faces using OpenCV videocapture in local. For Webapp , OpenCV can’t be used. Thus, using Streamlit-Webrtc for front-end application.

## Deployment of Streamlit WebApp in Google Cloud Platform and Streamlit
Deployment in cloud platform:-
Google Cloud Platform (GCP), offered by Google, is a suite of cloud computing services that runs on the same infrastructure that Google uses internally for its end-user products.
Web application Deployed successfully, there is issue with streamlit component in GCP which results in automatic closing of web cam. In local system it runs very well. we have submitted demo video of web app which run in local system. 
Link of Deployment in GCP -  https://face-emotion-detection-2hy7xluvrq-el.a.run.app


## Conclusion
Finally we build the webapp and deployed which has training accuracy of 72.68% and test accuracy of 66.48% . If you see how works visit link : https://drive.google.com/drive/folders/1giZBtGU48f2z8v0tSSXJagwUgb9N5YyU

Link of Deployment in GCP -  https://face-emotion-detection-2hy7xluvrq-el.a.run.app
