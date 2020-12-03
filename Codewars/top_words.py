import re
from collections import Counter

def top_3_words(s):
    s = remove_all('', re.findall(r"[\w']*", s.lower()))
    c = Counter(s)
    return sorted(c, key=lambda i: c[i], reverse=True)[:3]

def remove_all(sep, seq):
    return [w for w in seq if w != sep]

print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""))