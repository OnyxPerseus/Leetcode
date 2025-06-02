def encode(strs):
    res = ''
    for s in strs:
        res += str(len(s)) + '_' + s
    return res

def decode(s):
    res = []
    n = len(s)
    i = 0
    while (i<n):
        j = i + 1
        while (ord(s[j]) >= 48 and ord(s[j]) <= 58):
            j+=1
        count = int(s[i:j])
        i = j+1
        j += count + 1
        res.append(s[i:j])
        i = j
    return res

if __name__ == '__main__':
    strs = ["neet","code","love","you"]
    print(decode(encode(strs)))
