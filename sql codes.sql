create table netflix_database (
	  n_id int,
      title varchar(100),
      main_genre varchar(50),
      release_year year,
      maturity_rating varchar(25),
      original_audio  varchar (100)

        );
        

    alter table netflix_database
    modify main_genre varchar(255), 
    modify maturity_rating varchar(255), 
    modify original_audio varchar(255)