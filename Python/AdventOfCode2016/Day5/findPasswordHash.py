import md5
index = 0
passwordCharCount = 0
hash = ""
doorId = "cxdnnyjw"
password = ""

while passwordCharCount < 8:
    hashKey = doorId+str(index)
    hash = md5.new(hashKey).hexdigest()
    allZero = True
    for charIndex in range (0,5):
        char = hash[charIndex]

        if char.isalpha() or (char.isdigit() and int(char) != 0):
            allZero = False
            break
        
    if allZero == True:
        passwordCharCount += 1
        password += hash[5]

    index += 1

print(password)