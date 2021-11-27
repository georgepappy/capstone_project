# A Movie Database

### Data Engineering Capstone Project

#### Project Summary

This project makes use of the approximately 57,000 movies listed on TMDB.org to implement a PostgreSQL Snowflake schema which includes data on each movie (obtained via an *a priori* API query to create JSON files which include details such as the top-credited actors, director(s) and writer(s)), TMDB average ratings, and additional data from another set of users who have rated and/or tagged these movies independent of TMDB.

##### Rationale for Choice of Tools and Technologies Used

As this datbase relies on fairly static (i.e. infrequently-updated) data, there was no compelling reason for a cloud-based or distributed processing-based solution. Moreover, Pandas was well-suited to the data cleaning tasks required, and the data volume was not excessive, so using a Pandas-Psycopg2-PostgreSQL solution made perfect sense and runs quite well and in a timely manner.

##### Proposed Frequency of Data Updates

For a database of this sort, there is no strong justification for updating things any more frequently than once a week (which is exactly what IMDB.com does). This follows from the fact that movie and TV data are publicly reported on a weekly basis in the entertainment industry. Given how fast the processing pipelilnes above operate, there should be no problem in following such a schedule (the few minutes of downtime would hardly be noticed, escpecially given the non-mission-critical nature of this database/service).

A complete, step-by-step writeup of the project and its details can be found in the main project notebook here: https://github.com/georgepappy/capstone_project/blob/main/CapstoneProject_GeorgePappy.ipynb