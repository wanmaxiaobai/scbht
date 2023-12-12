import random
def randomsubsequence(datatrain,zxln):
    n = zxln
    data = datatrain
    data = data['d'].values.tolist()
    ls = []
    kn = 0
    for i in data:
        sl = i.split()
        if(len(sl)<n):
            continue
        start_index = random.randint(0, len(sl)-n)
        random_subsequence = sl[start_index: start_index + n]
        s = ' '.join(random_subsequence)
        # print(s)
        ls.append(s)
    return list(set(ls))


def generate_random_strings(char_list, num_runs, length):
    # 生成随机字符串的函数
    def random_string():
        # 打乱字符列表的顺序
        random.shuffle(char_list)
        # 从打乱顺序后的字符列表中选择指定长度的元素，并将其连接成字符串
        return ' '.join(char_list[:length])

    # 调用生成随机字符串的函数，运行num_runs次，并将结果存储在列表中
    result_list = [random_string() for _ in range(num_runs)]
    return result_list