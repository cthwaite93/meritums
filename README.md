# Meritums

This little program assigns candidates to their respective specialties. Specialties have a limited capacity and the member are in order by descent taking into account **points** they have.

## Data

The data is taken from a .json file created by the following website: https://www.sindicat.net/llistat-provisional-concurs-de-merits-2022-2023/. You can make a GET Request and get all the candidates in one single file.
As you will be able to see, that means we have **62937 records**, which maches the lists in the official [Generalitat lists](https://educacio.gencat.cat/web/.content/home/arees-actuacio/professors/oposicions/ingres-acces-cossos-docents/concurs-merits/valoracio-provisional/llista-provisional-merits-cos-especialitat.pdf)

### Data treatment

Because the data in this list doesn't have the parcial DNI *(Spanish ID)*, I had to figure out a way to identify a candidate. As you can see, candidates can make as many entries they want to different lists, and they decided a priority with each list. So first I parsed the data to find if there were more than two candidates with the same **full name** and priority **1**. Due to my luck, and people having similar surnames, there were loads of conflicts. That meant that I couldn't tell who was who **(BAD)!**
\ 
So by looking at the conflicts, I realized that it looked like that candidates with the same full name were in different tribunals *(phew)*. I decided to implement a custom identification by concatenating the full name and tribunal:

https://github.com/cthwaite93/meritums/blob/bbe6589b115f5018fcba299c185d7eacbabd258f/classes/candidate.py#L13

Well that left me with one conflict...so I edited the data and some Judit is *Judit2*.

## Algorithm

So, to the real interesting part: **How do I assign candidates to their respective specialty?** 
\
\
Now, one would say: *Well, let's get every candidates first priority, sort them by points and add them in their speciality.*
\
**BUT**, and it's a big but, that wouldn't be fair. What if someone had more points than another one but with a lower priority. I personally think that anyone is entitled to try and access any speciality if they can and their **merits** is what counts not their priority.
\
\
So what I do is the following:
* Put all the candidates in one list.
* Order them by ascending priority and if they are equal, by descending points.
https://github.com/cthwaite93/meritums/blob/bbe6589b115f5018fcba299c185d7eacbabd258f/classes/candidate.py#L15-L20
* The algorithm won't stop until the candidates list is empty, that means that all candidates have had the chance to be members of a specialty taking into account their priorities.
* We take a candidate and assign them to the specialty of their choice, unless the candidate has already been assigned to a specialty.
    - If the candidate is not assigned because they have already been assigned, that try goes to a waiting list in case they get kicked out down the way.
* If there's space in the specialty list, in they go. 
    - If not, we see if the last member of the list has less points than the candidate, and replace that member.
    - **IF THEY HAVE EQUAL POINTS, I PRIORITIZE THEIR PRIORITY AND IF IT'S THE SAME I LEAVE THE ONE ON THE LIST, DON'T HAVE ENOUGH DATA TO SORT THAT OUT.**
    https://github.com/cthwaite93/meritums/blob/bbe6589b115f5018fcba299c185d7eacbabd258f/classes/specialty.py#L15-L29
* If by adding a new candidate we've kicked out someone, we check if some of the candidate's tries are in the non-tested list, we add them again into the candidates list so they have a chance to be assigned to a specialty.

\
It all runs in under 2s, I'm pretty happy about it.

## Results
You have all the generated specialties lists in a folder. They are .csv files.
