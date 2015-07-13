# DCI Scores Bot
A python wrapper for [DCI](http://www.dci.org) that posts the most recent scores to reddit. 

## To install
Clone the repo and install the requirements.

    pip install -r requirements.txt
    
Create a `config.py` file that has two values:
* `username` = reddit username
* `password` = reddit password

Run `main.py` (presumably in a cron job)

## TODO
- [x] Write bot that can post to reddit
- [x] Check DCI scores every two minutes
	- [ ] Save shows to DB
- [x] Parse DCI Scores
	- [x] Check if new show
	- [ ] Parse to DB
	- [x] Parse to reddit
	- [ ] Parse to website
- [x] Submit to [/r/drumcorps](www.reddit.com/r/drumcorps)

