## What does this web app do?

Each year, there are many undergraduate students who are interested in doing summer research with professors. 
One of the most common methods of finding a professor is as follows:

- visit the university website with a list of professors from a specific department
- visit each professor's link, read their bio, research interest
- if a professor's research is interesting to the student, the student will email that professor

The problem with this approach is that there may be 50 or even 100 different professors on an university's faculty list website. It is tedious and time-consuming to do this.

To resolve this issue, Temitayo and Tim developed a prototype, in the form of a web crawler, to automate the process of seeking summer research positions and help students save time.  

### How it works:

- visit the website
- type in a research area in the search box (eg. software, security, systems)
- the web crawler will return ONLY the professors that match the given research area

### Please note:

This is only a prototype. It only works for the department of Computer Science at Carleton University.

## View this web app via:

http://instaprof-bold-wolf.mybluemix.net

## Before you run this web app locally, make sure you install:

- Python 3
  https://www.python.org/downloads/

- Flask
  http://flask.pocoo.org/docs/1.0/installation/
  
- Beautiful Soup
  https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup
  

##  Run the web app locally

**1)** Clone this repository

**2)** Inside the command line, change directory to:

```
ibm-intern-hackathon-2018
```

**3)** then run:
```
python main.py
```

**4)** visit:

```
http://localhost:8000
```
