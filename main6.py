#Count ovwels in string
def count_ovwels(text):
    count= 0
    for character in text:
        if(character in "aAeEiIoOuU"):
            count += 1
    return count
text = input("text: ")
count=count_ovwels(text)

print("Count: ", count)
