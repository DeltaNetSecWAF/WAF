import re

blackList = [
    [r"j\s+a\s+v\s+a\s+s\s+c\s+r\s+i\s+p\s+t"],
    [r"<script>"],
    [r"</script>"],
    [r"<body>"],
    [r"</body>"],

]

for pattern in blackList:
    pattern = re.compile(pattern)

'''
Scans the input for any patterns in the blacklist 
returns true if any pattern is found
false if no possible xss detected
'''
def xssScan(input):
    pos = 0
    while pos < len(input):
        for pattern in blackList:
            found = pattern.search(input, pos)
            if found:
                return True, "possible xss injection detected."
    return False

