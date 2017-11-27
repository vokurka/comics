# Comic book publishing in US

## Question
I wondered what is the number of different comic books published in US. You know, this kind of thing you do not usually ask. All the different pages are describing volume sold, which gives you rough idea about the size of market. But it does not specifically say what is the number of different comic books published. That is what I wanted to find out.

## Analysis
I found a great site with the history of all comic books published in US. It is called Previews World and you can find their Archive [here](https://www.previewsworld.com/NewReleases/Archive). 

I wanted to create a reproducible research, so I am going to describe all steps I took, including source codes of scripts. Step by step explanation follows.

From the site with links it was only a step to download all the archives, one link at a time, using a script (see 1st_step.sh).

After downloading all files for all years I created finite state machine (see 2nd_step.py), which parsed TSV files with multiple tables into the JSON format. This was particularly fun thing to do as the TSV are not valid.

After conversion to JSON format, I had to clean the list a bit, decode datetimes and put it all into CSV file and generate quick overview of the numbers. This can be found in step 3 (see 3rd_step.py).

## Conclusion
After crunching all numbers and records from the CSV (more than 43 000 records, see data.csv in 3rd_step folder) the results are surprising. I focused only on year 2016 (because this is year has complete data) and ignored merchandising (I am not interested in that). As a result, I got following numbers.

**In the year 2016 there were in total 16 034 published comics and graphics novels, books and magazins. Out of the total number, 14 848 were comics and graphics novels, 818 books and 368 magazines. Out of 14 848 comics and graphics novels, 1 939 were published by DC Comics and 2 145 published by Marvel Comics.**