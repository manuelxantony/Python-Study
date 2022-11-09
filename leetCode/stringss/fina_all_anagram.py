# https://leetcode.com/problems/find-all-anagrams-in-a-string/

def find_anagrams(s, p):
    if len(p) > len(s): return []
    p_count, s_count = {}, {}
    for i in range(len(p)):
        p_count[p[i]] = 1 + p_count.get(p[i], 0)
        s_count[s[i]] = 1 + s_count.get(s[i], 0)

    res = [0] if p_count == s_count else []
    l = 0
    for r in range(len(p), len(s)):
        s_count[s[r]] = 1 + s_count.get(s[r], 0)
        s_count[s[l]] -= 1

        if s_count[s[l]] == 0:
            s_count.pop(s[l])

        l += 1
        if s_count == p_count:
            res.append(l)

    return res

if __name__ == '__main__':
    s = 'cbaebabbacd'
    p ='abc'
    ans = find_anagrams(s, p)
    print(ans)