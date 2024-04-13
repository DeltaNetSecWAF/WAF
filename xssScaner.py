import re

cat = re.compile(r"(\'|\")\s+\+\s+(\'|\")").pattern

blackList = [
    #following patterns are base of researching the samy worm
    #https://samy.pl/myspace/tech.html
    [r"j\s+a\s+v\s+a\s+s\s+c\s+r\s+i\s+p\s+t"], #some browser may strip white space 
    [r"<script>"], #don't allow scripting
    [r"</script>"],
    [r"<body>"],#don't allow user to define a body  
    [r"</body>"],
    [r"innerHTML"],
    [rf"i(?={cat})n(?={cat})n(?={cat})e(?={cat})r(?={cat})H(?={cat})T(?={cat})M(?={cat})L"]
]

for pattern in blackList:
    pattern = re.compile(pattern)

'''
Scans the input for any patterns in the blacklist 
returns true if any pattern is found
false if no possible xss detected
'''
def Scan(input):
    pos = 0
    while pos < len(input):
        for pattern in blackList:
            found = pattern.search(input, pos)
            if found:
                return True
    return False

