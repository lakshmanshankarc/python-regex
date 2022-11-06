# Regular Expressions
[Python](https://python.org)
## This repository Will contains information about the Regular Expression in python

Regular Expression in programming is used to search through characters of text
It allows us to search through the text for validation(find and replace)

A regular expression is a sequence of characters that specifies a search pattern in text


```py
import re
```
importing the regular expression

### Python Regex functions

Python Regular Expressions supports four main functions

```py
re.findall() -> # List containing all the matched results
re.search() ->  # Returns a Match Obj if match is in the string
re.split() ->   # return a list where split match
re.sub() ->     # Replaces one or many matches
```
[W3Schools](https://w3shools.com/python/python_regex.asp)

## Basic (search.py)

```
[] Set of characted [a-z] (lowerCase) [a-nA-z] (lowercase a-n Or upperCase A-z)
^   Starts with
$   Ends with
.*  zero or more occurences
.+  one or more occurences
.{} Exact Number of Occurences
|   OR operator
```

## Special Sequences

```
\A{word} Begging of the Text
\b{} Starts with 
\B{} Search but not at Beggining or Ending
\d   Search for Integers
\z{} Ends with
```

## Sets
