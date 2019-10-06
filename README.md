# Faces based ID System

As machine learning and especially computer vision becomes more ubiquitous technology, we leveraged state-of-the-art algortihms to create system for face recognition, which can be used out of the box. The system has to be populated with people's images and names. Then machine learning algorithm has to spend time for training and evaluation results. After that, the system is ready to use.  

## Product Misson
Make out-of-the-box solution for face recognition.  Build an iOS app which is able to capture image of a person and then match images in database, if avaliable then the user could get access to the sysytem.

## Target Users
Schools (Classroom Access, Dormitories), Libraries, Companies (Educational Testing Services), Residents (Visitor Access Control),etc.

## User stories
I, a building’s administrator, want to improve security by implementing access system based on face recognition.
I, a lector, want to track class attendance using reliable method and without spending much time.
I, a hospital associate, want to identify a person who has a accidence without documents to facilitate the hospital check-in process.
I, an apartment owner, want to define the list of people who allowed to enter.
I, a representative of Education Testing Services, want to authenticate a person before they start the exam.

## Minimum Viable Product(MVP)
The system which can authenticate and authorize access to premises based on face recognition.

## Competitors
* STONELOCK
Website: https://www.stonelock.com/
"StoneLock technology uses multiple sources of non-visible wavelengths that are safe and allow for measurement of spectroscopic features below the skin in order to generate unique biometric metadata for each user."
* Facekey
Website: https://www.facekey.com/
* Suprema
Website:https://www.supremainc.com/en/solutions/facial-recognition-system.asp
"Suprema's facial recognition technology detects changes in the surrounding environment. By controlling near-infrared LED according to the surrounding brightness, it is possible to authenticate users from a dark room and even outdoors."
## Patent Analysis
* Amazon: Rekognition
The Rekognition technology could one day scan your face, identify who you are, use visual cues to figure out the kind of work you do, and potentially track you as you move around.http://appft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&d=PG01&p=1&u=%2Fnetahtml%2FPTO%2Fsrchnum.html&r=1&f=G&l=50&s1=%2220190050629%22.PGNR.&OS=DN/20190050629&RS=DN/20190050629
* Google: Face detection and recognition 
https://patents.google.com/patent/US9639740B2/en
* Apple: Presence Sensing and Facial Recognition for Macs
The computing device may be configured to determine when a user arrives or enters into proximity with the computing device and/or a probability that the user is present based on sensor input. In response to a positive determination that the user is present or upon achieving a threshold probability that the user is present, the device may power up, exit a sleep mode, and/or provide some feedback to the user.https://www.patentlyapple.com/patently-apple/2019/08/apple-wins-patent-for-presence-sensing-and-facial-recognition-for-macs.html

## System Design
https://www.lucidchart.com/documents/edit/ada73da8-d447-4a67-bebc-ef268805a659/0_0?shared=true&docId=ada73da8-d447-4a67-bebc-ef268805a659

## Technology
### Language: Python
* All team have experience on python.
* Easy to develop and test.
### User Interface: Core ML
Pros: 
* Core ML provide a framwork that allow the user to simply integrate machine learning models into App.
* Users can use a wide variety of other machine learning libraries and then use CoreML Tools to convert the model into the Core ML format. 
* It supports vision for analysis images.
* It's easy to call Mac camera.
## Facial Recognition: OpenCV/Tensorflow
The facial recognition progress is accomplished by following steps:
1. Data Gathering: Gather face data (face images in this case) of the persons you want to identify.
2. Train the Recognizer: Feed that face data and respective profile of each face to the recognizer so that it can learn.
3. Recognition: Feed new faces of that people and see if the face recognizer you just trained recognizes them.

OpenCV
Pros:
* OpenCV provide wide liabraries for image processing.
* Support Python
Cons:
* Have to decide on the features to extract then use ML to recogniaze faces according to the feartures.

Alternative :Tensorflow
Pros: 
* Algorithm is based on data.
* The neural networks can alleviate the problem of choosing and extracting features manually.

### Dataset: costom dataset
Since the product mission is improve the security of access to system, we'll instead want to recognize faces that are not part of any current dataset and recognize faces of people who already registered in the system. So we have to create a costom facial recognition dataset.

Method:OpenCV and webcam
Pros:
* More images used in training, the better! We can gather images for each person as much as we want.
* Can gather example face image in different lighting conditions,different times of day, different moods and emotional states.
* Typical for companies, schools, or other organizations where people need to physically show up and attend every day.
Cons:
* Need to have physical access to a particular person to gather example images of their face.

# Test
