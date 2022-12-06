DATASTREAM = "day6_input.txt"
with open(DATASTREAM, 'r') as file:
    data = file.read().rstrip()

def findMarkerPosition(datastream : str, length: int):
    for char in range(0, len(datastream), 1):
        charSet = set(datastream[char:char+length])
        if(len(charSet) == length):
            return char+length

print(findMarkerPosition(data, 4))
print(findMarkerPosition(data, 14))