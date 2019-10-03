# imdb-clone
An IMDB Clone repository

please follow the process sorted below

1. start an environment with requirements
2. migrate
3. createsuperuser
4. loaddata data.json

there you go..

P.S:
1. you may follow the process as the ordering defined or there may be problems with user related data  
2. for debugging purposes, the app has django-debug-toolbar installed.


NOTES for the "Bad vs. Good Queries Comparison 1":
   I have asked it on https://stackoverflow.com/questions/58211627/how-to-correctly-perform-django-queries-of-manytomany-fields

    there are two identical pages for movie lists: (home, latest movies, top movies and movies by genre)

    one team of pages has BAD query performance and other has GOOD ones 

    there are four fields of Movie. all four have MTM relationship with Celebrity Model:
        crews vs. casts, directors, writers

    one with bad queries has an idea of removing all three MTM fields (casts, directors, writers) of Movie Model
    and creating one MTM field named crews. The crews MTM has an intermediate model called MovieCrew which
    has a field called duty (with FK to Duty). duty field distinguishes casts, directors and writers. so 
    there should be no need to call all three groups from database. just one call should has been adequate.
    but it didn't work as expected.




