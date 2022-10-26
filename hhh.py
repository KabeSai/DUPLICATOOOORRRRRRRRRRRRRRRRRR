import string
def duplicate(line:str):
    counter = 0
    line = line.lower()
    for char in set(list(line)):
        if line.count(char) > 1:
            counter += 1
            print(char)
    return counter
print(duplicate("ААББвАвыалдлтакщ"))