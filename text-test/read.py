texts = {}

with open("text.txt") as f:
    for line in f:
        (key,val) = line.split(" : ")
        texts[key] = val

print(texts["banana"])
print(texts["killme"])
