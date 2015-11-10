# Lottery List Generator
_By Gary Pang, "CodeWritingCow"_


## What It Does
This Python program produces a txt file of lottery winners within the coverage area of the Press Enterprise daily newspaper in northeastern Pennsylvania. I am a reporter who wrote this program to make my work easier. Every month, I had to read a 200-page report for an hour to find local winners' names. Now, this program can do that in less than a second!


## How It Works
It opens a csv file (ex. rtk_pr01prizeclaimantreport_201405.csv) with information like this:

JOHN KARCHER,BLOOMSBURG,COLUMBIA,PA,"$1,000,000 DIAMOND DAZZLER","$1,000.00"

And makes a new txt file (rtk_pr01prizeclaimantreport_201405.txt) like this:

* John Karcher, $1,000 from $1,000,000 Diamond Dazzler


## Requirements
Get a monthly list of winners from the Pennsylvania Lottery by making a Right to Know request. The list is a pdf file, so it must be converted into csv. I use www.cometdocs.com for file conversions.


## Things to Work on
* Count number of winners per municipality.
* Sort lists of municipalities in alphabetical order.
* Sort winners' last names alphabetically.
* Convert pdf into csv.