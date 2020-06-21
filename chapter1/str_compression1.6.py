def compress(s):
    """
    :param s: string of characters i.e aabbbcddd
    :return: compressed string a2b3cd3
            if compressed version is longer than return original string
    """
    curr = s[0]
    count = 0
    out = ""
    for ele in s:
        if ele != curr:
            out += curr + str(count)
            curr = ele
            count = 1
        else:
            count += 1
    out += curr+str(count)
    if len(out) > len(s):
        return s
    return out


print(compress("aabbbcddd"))
print(compress("abcd"))
