def ismatch(s,p):
    for i in range(0,len(p)):
        if p[i]==s[i] or p[-i]=="*" or p[i]==".":
            return("match")
        else:
            return("no match")
print(ismatch("aa","pp"))

def is_match(s, p, i):
    x = False
    if p[i] == s[i] or p[-1] == "*" or p[i] == ".":
        x = True
    else:
        x = False
    if i <= len(p):
        i = i + 1
        is_match(s, p, i)
    return x


print(is_match("aa", ".q", 0))
"""
s ="aa"
p = "a.

memory_s = .
memory_p = p
"""


def is_match(s, p, i, j, memory_s, memory_p):
    if i >= len(s):
        return True
    if j < len(p) and i < len(s) and s[i] == p[j]:
        return is_match(s, p, i + 1, j + 1, memory_s[i], memory_p[j])
    elif j >= len(p) and i <= len(s) and memory_p == "*":
        return True
    elif j < len(p) and i < len(s) and (p[j] == "*" or (memory_s == memory_p or memory_p == "*" or memory_p == ".")):
        return is_match(s, p, i + 1, j + 1, memory_s[i], memory_p[j])
    elif j < len(p) and i < len(s) and p[j] == ".":
        return is_match(s, p, i + 1, j + 1, memory_s[i], memory_p[j])
    else:
        return False


s = 'aa'
p = 'a*'
print(is_match(s, p, 0, 0, s[0], p[0]))
