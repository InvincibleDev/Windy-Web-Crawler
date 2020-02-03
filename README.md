# Project Title

Windy-Web-Crawler is a Web Crawler that Crawls "www.windy.com" for Temperature and Wind speed details of a given place. Windy-Web-Crawler is a Command Line tool.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Installing

A step by step guide for installing from PyPi:

```
pip install windy-crawler
```


Usage :
```
>>> from windy_crawler.windy_web_crawler import windy

>>> windy("Place Name")

```
Example

```
>>> from windy_crawler.windy_web_crawler import windy

>>> windy("Bangalore")
******************************
Place :  Bengaluru, Karnataka, India
Latitude 12.97194
Longitude 77.59369

 On Sunday 2:

+-----------------------+-----+------+-----+-----+-----+
|          Hour         | 9AM | 12PM | 3PM | 6PM | 9PM |
+-----------------------+-----+------+-----+-----+-----+
| Temperature (celcius) | 20° | 26°  | 28° | 27° | 23° |
|      Wind (knots)     |  10 |  9   |  7  |  8  |  9  |
+-----------------------+-----+------+-----+-----+-----+

 On Monday 3:

+-----------------------+-----+-----+-----+-----+------+-----+-----+-----+
|          Hour         | 0AM | 3AM | 6AM | 9AM | 12PM | 3PM | 6PM | 9PM |
+-----------------------+-----+-----+-----+-----+------+-----+-----+-----+
| Temperature (celcius) | 20° | 18° | 16° | 20° | 27°  | 30° | 28° | 22° |
|      Wind (knots)     |  8  |  7  |  5  |  5  |  6   |  6  |  7  |  9  |
+-----------------------+-----+-----+-----+-----+------+-----+-----+-----+

 On Tuesday 4:

+-----------------------+-----+-----+-----+-----+------+-----+-----+-----+
|          Hour         | 0AM | 3AM | 6AM | 9AM | 12PM | 3PM | 6PM | 9PM |
+-----------------------+-----+-----+-----+-----+------+-----+-----+-----+
| Temperature (celcius) | 19° | 16° | 15° | 18° | 27°  | 29° | 27° | 22° |
|      Wind (knots)     |  10 |  8  |  5  |  6  |  8   |  6  |  6  |  7  |
+-----------------------+-----+-----+-----+-----+------+-----+-----+-----+

 On Wednesday 5:

+-----------------------+-----+-----+-----+-----+------+-----+-----+-----+
|          Hour         | 0AM | 3AM | 6AM | 9AM | 12PM | 3PM | 6PM | 9PM |
+-----------------------+-----+-----+-----+-----+------+-----+-----+-----+
| Temperature (celcius) | 20° | 17° | 17° | 19° | 26°  | 29° | 28° | 22° |
|      Wind (knots)     |  9  |  8  |  7  |  5  |  2   |  4  |  4  |  6  |
+-----------------------+-----+-----+-----+-----+------+-----+-----+-----+

 On Thursday 6:

+-----------------------+-----+-----+-----+-----+------+-----+-----+-----+
|          Hour         | 0AM | 3AM | 6AM | 9AM | 12PM | 3PM | 6PM | 9PM |
+-----------------------+-----+-----+-----+-----+------+-----+-----+-----+
| Temperature (celcius) | 20° | 17° | 15° | 19° | 28°  | 30° | 29° | 23° |
|      Wind (knots)     |  6  |  5  |  3  |  2  |  2   |  3  |  2  |  6  |
+-----------------------+-----+-----+-----+-----+------+-----+-----+-----+

 On Friday 7:

+-----------------------+-----+-----+-----+-----+------+-----+-----+-----+
|          Hour         | 0AM | 3AM | 6AM | 9AM | 12PM | 3PM | 6PM | 9PM |
+-----------------------+-----+-----+-----+-----+------+-----+-----+-----+
| Temperature (celcius) | 20° | 18° | 17° | 21° | 27°  | 30° | 29° | 26° |
|      Wind (knots)     |  7  |  5  |  4  |  4  |  4   |  4  |  3  |  3  |
+-----------------------+-----+-----+-----+-----+------+-----+-----+-----+

```
## Authors

[Ganesh Prasad B G](https://www.github.com/InvincibleDev)
