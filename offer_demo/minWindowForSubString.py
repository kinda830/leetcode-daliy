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
        for i in t:
            t_fre.setdefault(i, 0)
            t_fre[i] += 1

        distance = len(t)
        min_length = len(s) + 1

        begin = 0

        left = 0
        right = 0
        while right < len(s):
            char_right = s[right]
            if t_fre[char_right] > 0:
                distance -= 1

            t_fre[char_right] -= 1
            right += 1

            while distance == 0:
                if right - left < min_length:
                    min_length = right - left
                    begin = left

                char_left = s[left]
                if t_fre[char_left] == 0:
                    distance += 1

                t_fre[char_left] += 1
                left += 1

        if min_length < len(s) + 1:
            result = s[begin:begin + min_length]

    return result


if __name__ == "__main__":
    s = "ABAACBAB"
    t = "ABC"
    print(min_window(s, t))
