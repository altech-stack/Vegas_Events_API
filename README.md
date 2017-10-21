# Vegas EDM Event Scraper 

This project is a beginner's project to get you started with mongo, flask, and requests. For a tutorial on how to use this, visit: https://www.andrewlien.com/random-bits-of-code/2017/10/21/so-you-want-to-write-a-simple-api

## Getting Started

You're going to want a mongo instance. Either use docker mongo, or install mongo on your host to get started. 


### Prerequisites

What things you need to install the software and how to install them

```
pip install requests flask pymongo
```


## Deployment

To populate database:

```
python event_fetcher.py

```
To run flask server:

```
python vegas_api.py
```

Visit http://localhost:5000/api/<date_you_chose> in your browser. Ex:
```
http://localhost:5000/api/10-31-2017
``` 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* My workplace Exabeam (and my manager!) for improving my python knowledge
