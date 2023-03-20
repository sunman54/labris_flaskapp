# labris_flaskapp


## database commands for creating tables :


### Users table : 
```SQL
CREATE TABLE users (id serial PRIMARY KEY,
            
                                 username varchar (50) NOT NULL,
            
                                 firstname varchar (50) NOT NULL,
                                 middlename varchar (50),
                                 lastname varchar (50) NOT NULL,
                                 birthdate date,
            
                                 email varchar (150) NOT NULL,
                                 password varchar (200) NOT NULL,
                                 UNIQUE(username),
                                 UNIQUE(email)
                                 
                                 ) 
                                 
                                 
                                 ;

```


### loged_in_users table : 


```SQL
CREATE TABLE loged_in_users (id serial PRIMARY KEY,
                    username varchar (50),
                    login_time varchar (50),
                    login_date varchar (50));

```
