# Newsfeed

Get your news without ever having to leave the terminal!

[![Build Status](https://travis-ci.com/AlexanderJDupree/newsfeed.svg?branch=master)](https://travis-ci.com/AlexanderJDupree/newsfeed)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/AlexanderJDupree/newsfeed/blob/master/LICENSE)

## Introduction

The **Newsfeed** application provides a simple way to get the top news headlines at your terminal! This project was designed as a personal educational experience to refresh my skills in python, learn the basics behind docker, set up CI/CD, and integration with a RESTful API. 

## Getting Started

There are a few ways to get the **Newsfeed** application. But the first thing you'll need to do is get yourself a **Free** *News API* key. Get your *News API* key [here](https://newsapi.org/register). The **Newsfeed** app requires that the *News API* key be stored in the $NEWS_API_KEY environment variable. To do this put the following in your .profile or .bash_profile (or where ever you store your environment variables).  

```
export NEWS_API_KEY="your key here!"
```

### Clone this Repo

If you decide to run this application by cloning this repo you will also need to install the dependencies. To do this, run these commands:

```
git clone https://github.com/AlexanderJDupree/newsfeed.git
```
```
cd newsfeed && pip install -r requirements.txt
```

Once the requirements have been installed and the newsfeed has been added to $PATH, you're all set and all you have to do is run:

```
python newsfeed
```

Note: [python3](https://www.python.org/downloads/) install instructions. *pip* is included in python 3.4 or greater.

### Using the Docker image

Alternatively, if you don't have python/pip installed or don't know how to add a directory to the $PATH you can run the **Newsfeed** app with docker! With [docker installed](https://docs.docker.com/install/linux/docker-ce/ubuntu/) just run the following to pull the image and run the app.

```
docker pull dupree2022/newsfeed
```
```
docker run newsfeed
```

### Future Distributions

In the future I plan to ship **Newsfeed** with [pypi](https://pypi.org/). As well as instructions to build the newsfeed as a self-contained binary.  

### Usage 

Once **Newsfeed** is installed it can be used like any other POSIX command line program. As an example, heres how you can get the top 2 stories in the US related to Apple:

```newsfeed -t 2 -k apple```

Which will print out:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│ You Need to Update to iOS 12.2 Right Now to Fix More Than 50 Security Holes -    │
│ Gizmodo                                                                          │
│ Published At: 2019-03-26T14:22:00Z                                               │
│ ──────────────────────────────────────────────────────────────────────────────── │
│ Lost among Apple’s announcement of a new streaming TV service, subscription game │
│ service, and fancy new titanium credit card was the release of iOS 12.2. And     │
│ while the most significant new thing in iOS 12.2 is Apple’s updated News app,    │
│ anyone even remotely co…                                                         │
│ https://gizmodo.com/you-need-to-update-to-ios-12-2-right-now-to-fix-more-        │
│ th-1833572278                                                                    │
└──────────────────────────────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────────────────────────────┐
│ Tim Cook says Apple Card is a game changer. Experts are not so sure - CNN        │
│ Published At: 2019-03-26T14:14:00Z                                               │
│ ──────────────────────────────────────────────────────────────────────────────── │
│ Apple CEO Tim Cook said Monday that the tech company's new credit card would be  │
│ "the most significant change in the credit card experience in 50 years." But not │
│ everyone's buying it.                                                            │
│ https://www.cnn.com/2019/03/25/tech/apple-credit-card/index.html                 │
└──────────────────────────────────────────────────────────────────────────────────┘

                   Powered by News API (https://newsapi.org)                    
                      Contribute to make newsfeed better!                       
                  https://github.com/AlexanderJDupree/newsfeed                  
                                     v1.0.0  
```

## What's in this Repo?

Besides all the source files, there are a suite of unit tests as well. If you feel like contributing just make sure you add/update the unit tests in the test/ folder and open a pull request with the passing tests. To run the unit tests just cd into the newsfeed folder and type:

```
python -m unittest
```

If 0 tests are run, or there are failed imports then you are likely in the wrong folder. The unittest command should be run at one level above the test/ folder. 

## Built With

* [News API](https://newsapi.org/) - Powered by News API

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://raw.githubusercontent.com/AlexanderJDupree/BigInt/master/LICENSE) file for details

