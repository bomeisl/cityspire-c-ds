# CitySpire - Data Science

# Labs DS template

[Docs](https://docs.labs.lambdaschool.com/data-science/)

## Mission

Be a one-stop resource for users to receive the most accurate city information.

## Description

An app that analyzes data from cities such as populations, cost of living, rental rates, crime rates, park (walk score), and many other social and economic factors that are important in deciding where someone would like to live. This app will present such important data in an intuitive and easy to understand interface.

Use data to find a place right for you to live.


(provide FastAPI image and info on API endpoints)


## Data Engineering

FastAPI app, [deployed to Heroku](https://blahblahblah.herokuapp.com) and [deployed to AWS](https://blahblahblah.aws.com),
provides 2 routes. One route, `/labels`, provides the labels a user can select
to distinguish cities. The `/recommends` endpoint routes user input to the
machine learning model and returns the resulting recommendations.

A single endpoint that returns all data for a city in one object. 

Call an endpoint with a city request parameter, something like:
GET .../cities/the-big-city

then get a single object in return, something like:
{
   city_name: 'the-big-city',
   population: 1000000,
   rent_per_month: 1500,
   walk_score: {Idk what this should look like, up to you guys, just let us know},
   livability_score: {up to you as well}
}

| Type | Endpoint | Required Parameters | Returns |
| ---- | -------- | ---------- | ------- |
| GET  | /labels  |            | {'livability score': 100, 'rent rate': 500} |
| POST | /recommends | {'livability score': 100, 'rent rate': 1000} | {'Location': Miami Beach} |

More details about the API endpoints can be found at the
[ReDoc](https://blahblahblah.herokuapp.com/redoc) interface or by
exploring the interactive [SwaggerUI](https://blahblahblah.herokuapp.com).

## Machine Learning

Nearest Neighbors ML Model for CitySpire City Living Recommendations

The data wrangling and merging and can be found in the wrangling.ipynb notebook, while the tokening and TFIDF vectoring of text, creation of Nearest Neighbors model, training on tokenized and vectorized text, and pickling of Nearest Neighbors Model and TFIDF Vectorizer can all be found in the rec_modeling.ipynb notebook in the notebooks directory.

The Nearest Neighbors and TFIDF Vectorizer pickles can be found in the pickles directory.

The pickled Nearest Neighbors model and TFIDF Vectorizer are imported into recommend.py in the app directory so that they can be used in a recommend function in the Data Engineering API in order to recommend cities to live in to users based on desired population, rental rate, crime rate, walkability score, cost of living index, and livability score.

# Contributors

| John Dailey | Neha Kumari  | Theda | Mickey Wells |
| :---------: | :--------: | :--------: | :----------: |
| Data Scientist | Data Scientist | Data Scientist | Data Scientist |
| [<img src="https://github.com/favicon.ico" width="15">](https://github.com/johnjdailey) [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](https://www.linkedin.com/in/johnjdailey/) | [<img src="https://github.com/favicon.ico" width="15">](https://github.com/Neha-kumari31) [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](https://www.linkedin.com/in/neha-kumari-3325ba40/) | [<img src="https://github.com/favicon.ico" width="15">](https://github.com/LambdaTheda) [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](https://www.linkedin.com/) | [<img src="https://github.com/favicon.ico" width="15">](https://github.com/MickeyLeewells2020/) [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](https://www.linkedin.com/) |
