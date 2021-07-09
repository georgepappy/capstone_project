# DROP TABLES

user_actions_table_drop = "DROP TABLE IF EXISTS fact_user_actions;"
users_table_drop = "DROP TABLE IF EXISTS dim_users;"
time_table_drop = "DROP TABLE IF EXISTS dim_time;"
movies_table_drop = "DROP TABLE IF EXISTS dim_movies;"
actors_table_drop = "DROP TABLE IF EXISTS dim_actors;"
directors_table_drop = "DROP TABLE IF EXISTS dim_directors;"
writers_table_drop = "DROP TABLE IF EXISTS dim_writers;"


# CREATE TABLES

user_actions_table_create = ("""
                             CREATE TABLE IF NOT EXISTS fact_user_actions (
                             action_id serial PRIMARY KEY,
                             user_id int NOT NULL,
                             action_time timestamp NOT NULL,
                             movie_id int NOT NULL,
                             action varchar NOT NULL,
                             action_val varchar NOT NULL);
                            """)

users_table_create = ("""
                      CREATE TABLE IF NOT EXISTS dim_users (
                      user_id int PRIMARY KEY,
                      num_ratings int NOT NULL,
                      num_tags int NOT NULL,
                      avg_rating float);
                     """)

time_table_create = ("""
                     CREATE TABLE IF NOT EXISTS dim_time (
                     action_time timestamp PRIMARY KEY,
                     hour int, 
                     day int NOT NULL, 
                     week int NOT NULL, 
                     month int NOT NULL, 
                     year int NOT NULL);
                    """)

movies_table_create = ("""
                       CREATE TABLE IF NOT EXISTS dim_movies (
                       movie_id int PRIMARY KEY,
                       title varchar NOT NULL, 
                       tmdb_id int NOT NULL, 
                       imdb_id varchar NOT NULL,
                       genres varchar NOT NULL,
                       actor1_id int,
                       actor2_id int,
                       actor3_id int,
                       actor4_id int,
                       actor5_id int,
                       director1_id int,
                       director2_id int,
                       director3_id int,
                       director4_id int,
                       director5_id int,
                       writer1_id int,
                       writer2_id int,
                       writer3_id int,
                       writer4_id int,
                       writer5_id int,
                       release_date date,
                       runtime float,
                       tmdb_rating_avg float NOT NULL,
                       tmdb_votes_tot int NOT NULL);
                      """)

actors_table_create = ("""
                       CREATE TABLE IF NOT EXISTS dim_actors (
                       actor_id int PRIMARY KEY,
                       name varchar NOT NULL,
                       imdb_id varchar,
                       birthday date,
                       deathday date);
                      """)

directors_table_create = ("""
                          CREATE TABLE IF NOT EXISTS dim_directors (
                          director_id int PRIMARY KEY,
                          name varchar NOT NULL,
                          imdb_id varchar,
                          birthday date,
                          deathday date);
                         """)

writers_table_create = ("""
                        CREATE TABLE IF NOT EXISTS dim_writers (
                        writer_id int PRIMARY KEY,
                        name varchar NOT NULL,
                        imdb_id varchar,
                        birthday date,
                        deathday date);
                       """)


# INSERT RECORDS

user_actions_table_insert = ("""
                             INSERT INTO fact_user_actions (user_id, 
                             action_time, movie_id, action, action_val)
                             VALUES %s;
                            """)


users_table_insert = ("""
                      INSERT INTO dim_users (user_id, num_ratings, num_tags, avg_rating)
                      VALUES %s
                      ON CONFLICT (user_id)
                      DO NOTHING;
                     """)

time_table_insert = ("""
                     INSERT INTO dim_time (action_time, hour, day, week, month, year)
                     VALUES %s
                     ON CONFLICT (action_time)
                     DO NOTHING;
                    """)

movies_table_insert = ("""
                       INSERT INTO dim_movies (movie_id, title, tmdb_id, imdb_id,
                       genres, actor1_id, actor2_id, actor3_id, actor4_id, actor5_id,
                       director1_id, director2_id, director3_id, director4_id, director5_id,
                       writer1_id, writer2_id, writer3_id, writer4_id, writer5_id,
                       release_date, runtime, tmdb_rating_avg, tmdb_votes_tot)
                       VALUES %s
                       ON CONFLICT (movie_id)
                       DO NOTHING;
                      """)

actors_table_insert = ("""
                       INSERT INTO dim_actors (actor_id, name, imdb_id, 
                       birthday, deathday)
                       VALUES %s
                       ON CONFLICT (actor_id)
                       DO NOTHING;
                      """)

directors_table_insert = ("""
                          INSERT INTO dim_directors (director_id, name, imdb_id, 
                          birthday, deathday)
                          VALUES %s
                          ON CONFLICT (director_id)
                          DO NOTHING;
                          """)

writers_table_insert = ("""
                        INSERT INTO dim_writers (writer_id, name, imdb_id, 
                        birthday, deathday)
                        VALUES %s
                        ON CONFLICT (writer_id)
                        DO NOTHING;
                        """)


# QUERY LISTS

create_table_queries = [user_actions_table_create, users_table_create, time_table_create, movies_table_create, \
                        actors_table_create, directors_table_create, writers_table_create]

drop_table_queries = [user_actions_table_drop, users_table_drop, time_table_drop, movies_table_drop, \
                      actors_table_drop, directors_table_drop, writers_table_drop]