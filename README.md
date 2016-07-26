# scrapy-hh-ru
Scrapy example code.
## Install and run
Setup and activate virtualenv
```
virtualenv venv
source venv/bin/activate
```
Install requirements
```
pip install -r requirements.txt
```
Go to src dir and run crawler
```
scrapy crawl vacancies -o vacancies.csv -t csv
```
Open vacancies.csv.