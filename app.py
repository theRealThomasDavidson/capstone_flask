from flask import Flask
from functools import lru_cache
app = Flask(__name__)
current_version = "0.1.1"

@app.route('/version')
def version():
    """
    returns the version number of the app housed at this.site/version
    :return: a str that displays the current version
    """
    return "Version:{}".format(current_version)


@app.route('/ping')
def ping_pong():
    """
    responds to ping
    :return: a str "pong"
    """
    return "pong"


@app.route('/<num>')
def roman_route(num):
    """
    this acts both as the roman numeral converter and as a general junk collector
    :param num: a str that either is either an integer to turn into a roman numeral or garbage
    :return: a str either of a roman numeral responding to an int or a helpful reminder of the functions available
    """
    if num.isnumeric():
        return to_roman(int(num))
    return "Not Found", 404


@lru_cache(maxsize=None)
def to_roman(num):
    """
    converts ints into roman numerals and has a cache of stored previous answers
    :param num: an int ot be turned into a roman numeral
    :return: a str that shows the roman numeral that is equivilent to the number provided
    """
    if 0 >= num or num >= 4000:
        return "Number out of Bounds"
    rom = ""
    refs = (("M", 1000), ("CM", 900), ("D", 500),
            ("CD", 400), ("C", 100), ("XC", 90),
            ("L", 50), ("XL", 40), ("X", 10),
            ("IX", 9), ("V", 5), ("IV", 4), ("I", 1))
    ndx = 0
    while True:
        while num < refs[ndx][1]:
            ndx += 1
        rom += refs[ndx][0]
        num -= refs[ndx][1]
        if not num:
            return rom


if __name__ == '__main__':
    app.run(debug=True)
