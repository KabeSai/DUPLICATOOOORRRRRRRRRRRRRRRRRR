import string
import time

def timing(s):
    initial_time = time.time()
    duplicate(s)
    timing1 = time.time() - initial_time
    initial_time = time.time()
    count_duplicate(s)
    timing2 = time.time() - initial_time
    if timing2 < timing1:
        return (timing2, 2)
    return (timing1, 1)
def count_duplicate(s):
    return len([ch for ch in set(s.lower()) if s.lower().count(ch) > 1])
def duplicate(line:str):
    counter = 0
    line = line.lower()
    for char in set(list(line)):
        if line.count(char) > 1:
            counter += 1
    return counter

print(timing("ААББвАвыалдлтакщААББвАвыалдлтакщААББвАвыалдлтакщААББвАвыалдлтакщААББвАвыалдлтакщААББвАвыалдлтакщААББвАвыалдлтакщААББвАвыалдлтакщААББвАвыалдлтакщААББвАвыалдлтакщААББвАвыалдлтакщААББвАвыалдлтакщААББвАвыалдлтакщААББвАвыалдлтакщААББвАвыалдлтакщААББвАвыалдлтакщ"))