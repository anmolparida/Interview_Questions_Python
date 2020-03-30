
# vInput = input()
vInput = "a{d,c,b}e"


vStart = vInput.split('{')[0]
vEnd = vInput.split('}')[1]

vMid = vInput[vInput.find("{") + 1:vInput.find("}")]
vMidList = []

for midValue in vMid.split(','):
    vMidList.append(vStart + midValue + vEnd)

print(set(vMidList))  # prints with brackets




