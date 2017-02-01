import md5

index = 0
passwordCharCount = 0
hash = ""
doorId = "cxdnnyjw"
passwordSet = "00000000"
password = "00000000"


while passwordCharCount < 8:
    hashKey = doorId+str(index)
    hash = md5.new(hashKey).hexdigest()
    allZero = True
    for charIndex in range (0,5):
        char = hash[charIndex]

        if char.isalpha() or (char.isdigit() and int(char) != 0):
            allZero = False
            break
        
    if allZero == True and hash[5].isdigit():
        newIndex = int(hash[5])
        if newIndex < 8 and int(passwordSet[newIndex]) == 0:
            password = password[:newIndex] + hash[6] + password[newIndex+1:]
            passwordSet = passwordSet[:newIndex] + '1' + passwordSet[newIndex+1:]
            passwordCharCount += 1

    index += 1

print(password)