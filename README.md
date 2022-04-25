### Movie_Recommendation_Mania

- Django(Python framework) application to give you predictions based on your profile. 
- Movie data set is used from Netflix Sample data set to train prediction model. 
- User-User collabarative filtering with optimizations with region specific group to train model faster with less number of input points.

***How to use this project:***
- Download zip.
- Setup the machine with the requirements.txt at the root.
- Configure, connect and load data in the sqllite.
- Create Django project on your machine and replace required filed from the package. [Refer](https://docs.djangoproject.com/en/4.0/intro/tutorial01/#creating-a-project)
- Start Django Project on localhost using
```
>>> cd <path to project directory where manage.py is present>
>>> python manage.py runserver <8080 or any other port if this port is in use>
```

***Tech used:***
- Dataset: https://www.kaggle.com/laowingkin/netflix-movie-recommendation/data & TMDB dataset through API
- Framwork documentation: https://docs.djangoproject.com/en/4.0/
- SqlLite as db

***Screens:***
 ![Recommend from search](https://user-images.githubusercontent.com/20341930/165031664-cef76588-2647-4deb-b2ad-ee7c75964297.png)


*Note: Few packages might be outdated and might require you to refactor your code based on updates. I have taken down the application serveer for this project.*
