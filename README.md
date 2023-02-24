# Meritums

This little program assigns candidates to their respective specialties. Specialties have a limited capacity and the members are in order by descent taking into account the **points** they have.

### Disclaimer
The algorithm output is based on treated unofficial data and should be treated as such, all official data is in the link below.

## Data

The data is taken from a .json file created by the following website: https://www.sindicat.net/llistat-provisional-concurs-de-merits-2022-2023/. You can make a GET Request and get all the candidates in one single file.
\
As you will be able to see, that means we have **62937 records**, which matches the lists in the official [Generalitat lists](https://educacio.gencat.cat/web/.content/home/arees-actuacio/professors/oposicions/ingres-acces-cossos-docents/concurs-merits/valoracio-provisional/llista-provisional-merits-cos-especialitat.pdf).

### Data treatment

Because the data in this list doesn't have the parcial DNI *(Spanish ID)*, I had to figure out a way to identify a candidate. As you can see, candidates can make as many entries they want to different lists, whilst deciding a priority for each list. 
\
\
So first I parsed the data to find if there were more than two candidates with the same **full name** and priority **1**. Due to my luck, and people having similar surnames, there were loads of conflicts. That meant that I couldn't tell who was who **(BAD)!**
\
\
So by looking at the conflicts, I realized that it looked like candidates with the same full name were in different tribunals *(phew)*. I decided to implement a custom identification by concatenating the full name and tribunal:

https://github.com/cthwaite93/meritums/blob/5bb96bee51dab7e41685ca6cc4fa693d7d1084dd/classes/candidate.py#L10

Well that left me with one conflict...so I edited the data and some Judit is *Judit2*.

### Data parsing

Before we can get into how the algorithm works, you must know that the *"original"* data is parsed and modified to ease the processing of it. All candidate's records are merged into **one record per candidate**.
\
In that record, all the information of the candidate's attempts (scores and priorities), are kept for each of the specialties they are trying to get into.
\
By doing this we reduce the data from 62937 to **37333 records**.

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
* Order them by descent on their current attempt's points.
https://github.com/cthwaite93/meritums/blob/5bb96bee51dab7e41685ca6cc4fa693d7d1084dd/classes/candidate.py#L43-L44
    - A candidate's current attempt, is always the one with the highest priority which hasn't been tried to be inserted on a speciality.
* The algorithm won't stop until the candidates list is empty, that means that all candidates have had the chance to be members of a specialty taking into account their priorities.
* We take a candidate and assign them to the specialty of their choice.
* If there's still free places in the specialty, in they go. 
    - If not, we see if the last member of the list has less points than the candidate, and replace that member.
    - **IF THEY HAVE EQUAL POINTS, I PRIORITIZE THEIR PRIORITY AND IF IT'S THE SAME I LEAVE THE ONE ON THE LIST, DON'T HAVE ENOUGH DATA TO SORT THAT OUT YET.**
https://github.com/cthwaite93/meritums/blob/5bb96bee51dab7e41685ca6cc4fa693d7d1084dd/classes/specialty.py#L43-L70
* If by adding a new candidate we've kicked out someone, we check if the candidate has other attempts. 
* It that's the case we add them again into the candidates list so they have a chance to be assigned to another specialty.
\
\
It all runs in under 2 seconds, I'm pretty happy about it.

## Results
In the *lists* folder, you have a folder for each of the specialties that are going through the merits process.
\
\
Inside the specialties folder, you have the accepted.csv list, where you will find who has been accepted into the specialty.
\
Furthermore, you will find the rejected.csv list, where you will find those who have been rejected.
\
\
It is important to state, that *NO CANDIDATE* can be in more than one accepted list, and if they have been accepted they won't appear in any of the rejected lists *(makes sense)*.
\
\
On the other hand, a candidate **can appear** in one or more rejected lists.
