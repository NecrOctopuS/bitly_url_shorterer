# Bitly url shorterer

This project interacts with the site [bit.ly](https://bit.ly) for trimming links.
Your link is sent to the input, and a shortened link like bit.ly/****** is output.

You can also submit an already shortened link to the input, then the output will have the number of clicks on this link.

### How to install

Python3 should be already installed.
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).

### Script run examples

Your full link is sent to the input, the output is shortened link
```
py bitly_url_shorterer.py https://yandex.ru/support/navigator/refuel.html
Bitlink http://bit.ly/2mvkiXm
```
You can sent a shortened link to the input, then the output will be the number of clicks on this link
```
py bitly_url_shorterer.py http://bit.ly/2mvkiXm
Number of transitions: 1
```
There must be a link with a full prefix at the input, i.e. http: // ******** or https: // *******
```
py bitly_url_shorterer.py yandex.ru
Неправильная ссылка
```