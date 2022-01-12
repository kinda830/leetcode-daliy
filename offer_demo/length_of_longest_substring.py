'''
@filename		:lengthOfLongestSubstring.py
@Description	:求最长不重复子串的长度
@Date			:2022/01/12 10:41:05
@Author      	:hjd
@version      	:1.0
'''


def lengthOfLongestSubstring(s):
    ans = 0
    oss = set()
    if s:
        rk = -1
        for i in range(len(s)):
            if i != 0:
                oss.remove(s[i - 1])
            while rk + 1 < len(s) and s[rk + 1] not in oss:
                oss.add(s[rk + 1])
                rk += 1
            ans = max(ans, rk - i + 1)
    return ans


def length_sub_string(s):
    result = {}
    start, ans = 0, 0
    for end in range(len(s)):
        if s[end] in result:
            start = max(start, result[s[end]] + 1)
        result[s[end]] = end
        ans = max(ans, end - start + 1)
    return ans


if __name__ == '__main__':
    sentense = "abcdabcddcbasdk"
    print(length_sub_string(sentense))
