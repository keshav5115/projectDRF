Users
    admin
        username:admin
        password:admin1234
    enduser
        keshav:keshav1234
    can create new user either using browsable_api or using postman
        with url http://127.0.0.1:8000/user/register/
permissions
    1. admin
            can create a movie and edit or delete a review given by the enduser.
    2. only authenticate  user can give review to the movie.
    3. anyone can see the movies and reviews given by the users.

AUTHENTICATION
    Token authentication has been used 
        1. Token will be created when user register or login(if token not there)
        2. Token will be destroyed when user logout.

