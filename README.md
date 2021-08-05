# data collection pipeline
the need here is that you are required to conduct some data collection from the internet, say you're interested to see how the car price fluctuate across a certain duration

# purpose:
to create a pipeline that will feed into the database for data collected from external sources

# approach:
Data will be scraped and uploaded daily in an sql database. The work is split into three phases
1. Scraping (python)
2. Loading (python)
3. Automation (batch file)

Scraping phase will output a flat file daily. Loading phase will take the flat file from scraping phase and load into sql server. Automation phase relies on running the two python script in succesion and carried out by windows task scheduler.

# psa on scraping
always read robots.txt on the website by going http://yourwebsite/robots.txt, most website will have this file, and read their requirement
be courteous and space out the request to avoid overloading the server

#
