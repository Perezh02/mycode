#!/usr/bin/env python3

def main():
    zodiac_sign = {
            'Rabbit' : [2011, 1999, 1987, 1975, 1963],
            'Rat': [2020, 2008, 1996, 1984, 1972, 1960],
            'Tiger': [2010, 1998, 1986, 1974, 1962],
            'Ox': [2021, 2009, 1997, 1985, 1973, 1961],
            'Dragon': [2012, 2000, 1988, 1976, 1964],
            'Snake': [2013, 2001,1989, 1977, 1965],
             'Horse': [2014, 2002, 1990, 1978, 1966],
            'Sheep': [2015, 2003, 1991, 1979, 1967],
            'Monkey': [2016, 2004, 1992, 1980, 1968],
            'Rooster': [2017, 2005, 1993, 1981, 1969],
            'Dog': [2018, 2006, 1994, 1982, 1970],
            'Pig': [2019, 2007, 1995, 1983, 1971]

        }

    name = input("please enter you name:\n>")
    name = name.title()

    year =int(input("Please enter your birth year in YYYY format, e.g 2010:\n>"))

    for sign, years in zodiac_signs.items():
        if year in years:
            print(f"{name} your zodiac sign is {sign}, you are {get_traits(sign)}.")

    else:

 print("Sorry, your birth year is not in our records.")


def get_traits(sign):
    traits = {'Rabbit': 'vigilant, witty, quick-minded, and ingenious',
        'Rat': 'artistic, sociable, industrious, charming, and intelligent',
        'Tiger': 'courageous, enthusiastic, confident, charismatic, and a leader',
        'Ox': 'strong, thorough, determined, loyal, and reliable',
        'Dragon': 'talented, powerful, lucky, and successfull',
        'Snake': 'wise, like to work alone, and determined',
        'Horse': 'animated, active, and energetic',
        'Sheep': 'creative, resilient, gentle, mild-mannered, and shy',
        'Monkey': 'sharp, smart, curious, and mischievious',
        'Rooster': 'hardworking, resourceful, courageous, and talented',
        'Dog': 'loyal, honest, cautious, and kind',
        'Pig': 'a symbol of wealth, honesty, and practicality'
    }
    return traits[sign]

main()


