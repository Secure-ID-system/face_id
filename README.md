# Faces based ID System

As machine learning and especially computer vision becomes more ubiquitous technology, we leveraged state-of-the-art algortihms to create system for face recognition, which can be used out of the box. The system has to be populated with people's images and names. Then machine learning algorithm has to spend time for training and evaluation results. After that, the system is ready to use.  

# Product Misson
Make out-of-the-box solution for face recognition.  Build an iOS app which is able to capture image of a person and then match images in database, if avaliable then the user could get access to the sysytem.

# Target Users
Schools (Classroom Access, Dormitories), Libraries, Companies (Educational Testing Services), Residents (Visitor Access Control),etc.

# User stories
I, a building’s administrator, want to improve security by implementing access system based on face recognition.
I, a lector, want to track class attendance using reliable method and without spending much time.
I, a hospital associate, want to identify a person who has a accidence without documents to facilitate the hospital check-in process.
I, an apartment owner, want to define the list of people who allowed to enter.
I, a representative of Education Testing Services, want to authenticate a person before they start the exam.

# Minimum Viable Product(MVP)
The system which can authenticate and authorize access to premises based on face recognition.

# Competitors

# Patent Analysis

# System Design
https://www.lucidchart.com/documents/edit/ada73da8-d447-4a67-bebc-ef268805a659/0_0?shared=true&docId=ada73da8-d447-4a67-bebc-ef268805a659

# Technology
## Language: Python
* All team have experience on python.
* Easy to develop and test.
## User Interface: Core ML
Pros: 
* Core ML provide a framwork that allow the user to simply integrate machine learning models into App.
* Users can use a wide variety of other machine learning libraries and then use CoreML Tools to convert the model into the Core ML format. 
* It supports vision for analysis images.
* It's easy to call Mac camera.
## Facial Recognition: OpenCV
The facial recognition progress is accomplished by following steps:
1. Data Gathering: Gather face data (face images in this case) of the persons you want to identify.
2. Train the Recognizer: Feed that face data and respective profile of each face to the recognizer so that it can learn.
3. Recognition: Feed new faces of that people and see if the face recognizer you just trained recognizes them.

So in our project, we are going to use the algorithem provided by OpenCV.
Pros:
* OpenCV provide wide liabraries for image processing.
* Support Python

Alternative 
Tensorflow


## Dataset: costom dataset
Since the product mission is improve the security of access to system, we'll instead want to recognize faces that are not part of any current dataset and recognize faces of people who already registered in the system. So we have to create a costom facial recognition dataset.

Method:OpenCV and webcam
Pros:
* More images used in training, the better! We can gather images for each person as much as we want.
* Can gather example face image in different lighting conditions,different times of day, different moods and emotional states.
* Typical for companies, schools, or other organizations where people need to physically show up and attend every day.
Cons:
* Need to have physical access to a particular person to gather example images of their face.

# Test
