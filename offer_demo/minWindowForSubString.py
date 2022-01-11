'''
@file        :minWindow.py
@Description :最小覆盖子串
@Date        :2022/01/09 14:17:06
@Author      :kinda
@version     :1.0
'''


def min_window(s, t):
    result = ""

    if s and t:
        t_fre = {}
        for tt in t:
            t_fre.setdefault(tt, 0)
            t_fre[tt] += 1

        begin, left, right = 0, 0, 0

        distance = len(t)
        min_lenght = len(s) + 1

        while right < len(s):

            if s[right] in t_fre.keys():
                if t_fre[s[right]] > 0:
                    distance -= 1

                t_fre[s[right]] -= 1
            right += 1

            while distance == 0:
                if right - left < min_lenght:
                    min_lenght = right - left
                    begin = left
                if s[left] in t_fre.keys():
                    if t_fre[s[left]] == 0:
                        distance += 1

                    t_fre[s[left]] += 1
                left += 1

        if min_lenght < len(s) + 1:
            result = s[begin:begin+min_lenght]

    return result


if __name__ == "__main__":
    s = "ABTAACBAB"
    t = "ABC"
    print(min_window(s, t))
