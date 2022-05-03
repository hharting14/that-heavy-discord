# That Heavy Discord

*A discord-like app to talk about heavy music bands made with Django.*

![Screenshot_Home](https://user-images.githubusercontent.com/94148624/166558730-45031c37-a0d5-481f-b319-b1c74f28b1f7.png)

This project uses Django, PostgreSQL, and Docker.
*The project is inspired by the 7 hour Discord-clone tutorial available on Youtube made by Dennis Ivy.*

To run it, you must have Docker and Docker Compose installed locally. Clone this repository.
Then, go to the project folder and build the Docker image and run the project:
```
docker-compose build
docker-compose up
```
It should install all the requirements without any problems. Finally go to http://localhost:8000.

The project has the following functionalities:
1. Register/login/logout users.
2. User profile view and settings.
3. Create rooms with a specific topic (bands).
4. Browse by room topics.
5. Machine learning classifier for band predictions according to user's preferences. Here it can predict up to these 6 options: *Metallica, Slayer, Gojira, Kreator, Iron Maiden, Dream Theater.* The choices available for the ml model form can be found in the utils folder.
6. Edit/delete room options if you're the room host.


Here you can see a preview of how the project looks:

![Screenshot_Home](https://user-images.githubusercontent.com/94148624/166561601-2e67855c-e8b9-4c7e-aa90-2a70bddefd76.png)

![Screenshot_Create room](https://user-images.githubusercontent.com/94148624/166561652-82341cf5-48f7-45bc-85d4-76734308aad7.png)

![Screenshot_Room](https://user-images.githubusercontent.com/94148624/166561665-18e1b074-0bbd-4566-853a-9fdc24f6d6c7.png)

![Screenshot_Topics](https://user-images.githubusercontent.com/94148624/166561741-722fd280-bb17-4183-877b-fe5710f1b64a.png)

![Screenshot_Profile](https://user-images.githubusercontent.com/94148624/166561762-04a1c757-9a49-4f12-97c1-454f652b5678.png)

![Screenshot_Edit_Profile](https://user-images.githubusercontent.com/94148624/166561779-c7c9d23e-ebb3-4e91-bd3d-3de60c579b5d.png)

![Screenshot_ML_Form](https://user-images.githubusercontent.com/94148624/166562358-95a53f99-d2fe-41b3-beaa-f581402d946a.png)

![Screenshot_Prediction](https://user-images.githubusercontent.com/94148624/166561892-3ec6213b-7d7d-4180-8269-412c77603984.png)
