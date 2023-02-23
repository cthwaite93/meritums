# Meritums

This little program assigns candidates to their respective specialties. Specialties have a limited capacity and the member are in order by descent taking into account **points** they have.

## Data

The data is taken from a .json file created by the following website: https://www.sindicat.net/llistat-provisional-concurs-de-merits-2022-2023/. You can make a GET Request and get all the candidates in one single file.
As you will be able to see, that means we have **62937 records**, which maches the lists in the official [Generalitat lists](https://educacio.gencat.cat/web/.content/home/arees-actuacio/professors/oposicions/ingres-acces-cossos-docents/concurs-merits/valoracio-provisional/llista-provisional-merits-cos-especialitat.pdf)

### Data treatment

Because the data in this list doesn't have the parcial DNI *(Spanish ID)*, I had to figure out a way to identify a candidate. As you can see, candidates can make as many entries they want to different lists, and they decided a priority with each list. So first I parsed the data to find if there were more than two candidates with the same **full name** and priority **1**. Due to my luck, and people having similar surnames, there were loads of conflicts. That meant that I couldn't tell who was who **(BAD)!**
\ 
So by looking at the conflicts, I realized that it looked like that candidates with the same full name were in different tribunals *(phew)*. I decided to implement a custom identification by concatenating the full name and tribunal:

```python
    self.candidate_id = self.full_name + self.tribunal
```
