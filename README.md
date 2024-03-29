# COVID-19 Dashboard

![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)
![forthebadge](https://forthebadge.com/images/badges/check-it-out.svg)

![myimagen](/img/cover.jpeg)

## Table of Content

- [Introduction](#Introduction)
- [Goals](#Goals)
- [Data Cleaning](#Data-Cleaning)
- [Database](#Database)
- [API](#API)
- [Dashboard](#Dashboard)
- [How To Use It](#How-To-Use-It)
- [Credits](#Credits)


## Introduction

This is my Bootcamp Mid Project where I created a dashboard about COVID-19 in Germany and Venezuela. It is my first real project since I jumped into data analytics field. You are going to find how I did it and the goals that was setted at then end of it. I hope you like it 🤟

[Back to Table of Content](#table-of-content)

## Goals

### L1
- [X] Create Api in FastApi
- [X] Create Dashboard in streamlit
- [X] Database in **MongoDB** or PostgreSWL
### L2
- [ ] Use of geospatial data and geoqueries in MongoDB or Postgres (Using PostGIS)
- [X] Have the database in the Cloud (There are free services in MongoDB Atlas, Heroku Postgres, dentre others)
- [ ] Generate pdf report of the data visible in Streamlit, downloadable via button.
- [ ] A multi-page dashboard in Streamlit.
### L3
- [ ] Have the dashboard send you the pdf report by e-mail
- [ ] To be able to upload new data to the database via API (username and password as request headers)
### L4
- [ ] To be able to update the database via Streamlit (with username and password, in a separate page. The dashboard must make the previous request that adds data via API)
- [ ] Create Docker container and deploy the services in the cloud (Heroku. The two services must be uploaded separately)

[Back to Table of Content](#table-of-content)

## Data Cleaning

For this project I used this dataset from Kaggle [Time Series Data Covid-19 Global](https://www.kaggle.com/datasets/baguspurnama/covid-confirmed-global). You can find the csv files within data folder: confirmed_global.csv, deaths_global.csv and recovered_global.csv.

I did some data cleaning to get only cases form Germany and I dropped the Province/State column from the dataset because it was empty, at least for this country. Then, I created three new files as the original dataset but named different: germany_confirmed_cases.csv, germany_confirmed_deaths.csv and germany_confirmed_recovered.csv.

If you want yo explore how I did the data cleaning, check the file within data folder or clicking [here](/data/cleaning_data.ipynb).

[Back to Table of Content](#table-of-content)

## Database

The datasets cleaned was uploaded to Mongo DB as a CSV file for being processed through the API.

[Back to Table of Content](#table-of-content)

## API

I created an API with its routers to extract data when it is neccesary.

[Back to Table of Content](#table-of-content)

## Dashboard

The dashboard was created using [Streamlit](https://streamlit.io) interface.

[Back to Table of Content](#table-of-content)

## How To Use It

* Clone repository
* Run API

    ` uvicorn main:app `
* Run Streamlit

    ` streamlit run main.py `

[Back to Table of Content](#table-of-content)

## Credits

I'd like to thanks to my teachers [Santino Lede](https://github.com/Luxor5k) and [Daniel Alvarado](https://github.com/DanielDls-exe) for support me in each step of this project. Also, I want to thanks Nicolas Manduley [repository](https://github.com/nmanduley/midproject), because it helped me to chart my data.

[Back to Top](#covid-19-dashboard)

## Hi 👋 I'm Jesús Adraz!

### **Junior Data Engineer**

I am a Junior Data Engineer passionate about analyzing data, creating dashboards and data driven cultures.

### You can support my work clicking "☆ Star" on this repo or nominate to "GitHub Star". Thank you!

[![GitHub Star](https://img.shields.io/badge/GitHub-Nominate_to_star-yellow?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://stars.github.com/nominate/)

### Check my GitHub Profile to know more about me

[![Web](https://img.shields.io/badge/GitHub-JAdraz-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/JAdraz)