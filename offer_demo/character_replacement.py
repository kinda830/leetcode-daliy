'''
@file        :characterReplacement.py
@Description :给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度
@Date        :2022/01/09 22:42:01
@Author      :kinda
@version     :1.0
'''


def character_replacement(s, k):
    maxn, right, left = 0, 0, 0

    num = [0] * 26

    while right < len(s):
        num[ord(s[right]) - ord("A")] += 1

        maxn = max(maxn, num[ord(s[right]) - ord("A")])

        if right - left + 1 - maxn > k:
            num[ord(s[left]) - ord("A")] -= 1
            left += 1

        right += 1

    return right - left


if __name__ == "__main__":
    s = "ABAB"
    k = 2
    print(character_replacement(s, k))
