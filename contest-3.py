# You are given a string str that contains some Html text. In this Html text is an image URL that is in the tag.
# You need to extract the URL. The image URL is of the format .jpg.
import re


def imgExtracter(str):
    pat = r"w{3}.*[jpg]"
    mo = re.search(pat, str)

    return print(mo.group())


# You are given a string str of length >= 2. You need to extract the last 2 characters
# and print a new string that has the extracted characters 3 times concatenated.


def copyCat(str):
    s = ''
    for i in range(3):
        s += str[-2]+str[-1]
    return s

# You are given a string str. You need to print True if the str ends with boom else print False.


def boom(str):
    return str.endswith('boom')
