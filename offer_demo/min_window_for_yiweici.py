'''
@filename		:min_window_for_yiweici.py
@Description	:找到字符串中所有字母异位词，滑动窗口解法
@Date			:2022/01/11 14:20:39
@Author      	:hjd
@version      	:1.0
'''


def min_window(s, t):
    result = []
    left, right = 0, 0
    distance = len(t)
    t_fre = {}
    for tt in t:
        t_fre.setdefault(tt, 0)
        t_fre[tt] += 1

    while right < len(s):

        if s[right] in t_fre.keys():
            if t_fre[s[right]] > 0:
                distance -= 1
            t_fre[s[right]] -= 1

        right += 1

        while distance == 0:
            if right - left == len(t):
                result.append(left)

            if s[left] in t_fre.keys():
                if t_fre[s[left]] == 0:
                    distance += 1

                t_fre[s[left]] += 1

            left += 1
    return result


if __name__ == "__main__":
    s = "cbaebabacd"
    t = "abc"

    print(min_window(s, t))
