text1 = open("text1.txt", "r")
textDict1 = open("textDict.txt", "w")
textDict = {}
for line in open('text1.txt'):
    line = line.split()
for i in range(0, len(line)):
    check = line[i] in textDict
    if check is True:
        textDict[line[i]] += 1
    else:
        textDict[line[i]] = 1
for key, value in textDict.items():
    textDict1.write('{}:{}\n'.format(key, value))
