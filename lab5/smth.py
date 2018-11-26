def read_from_file():
    with open('graph.txt') as f:
        data = f.readline()
    data, pow_symbol = data.split()
    return data, int(pow_symbol)


def decToBinary(number):
    binary_list = [0] * number
    i = 0
    while number > 0:
        binary_list[i] = number % 2
        n = int(number / 2)
        i += 1
    n = ""
    for j in range(i - 1, -1, -1):
        # print(binary_list[j], end = "")
        n += str(binary_list[j])
    return n


NO_OF_CHARS = 256


def bad_char_heuristic(string, size):
    bad_char = [-1] * NO_OF_CHARS
    for i in range(size):
        bad_char[ord(string[i])] = i
    return bad_char


def search(txt, pat):
    substring_len = len(pat)
    string_len = len(txt)
    bad_char = bad_char_heuristic(pat, substring_len)
    s = 0
    while s <= string_len - substring_len:
        j = substring_len - 1
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1
        if j < 0:
            return s
            s += (substring_len - bad_char[ord(txt[s + substring_len])]
                  if s + substring_len < string_len else 1)
        else:
            s += max(1, j - bad_char[ord(txt[s + j])])


def power(string, n):
    length = len(string)
    binary = ""
    number = 0
    binary_array = []
    while len(binary) <= len(string):
        binary = decToBinary(pow(n, number))
        if len(binary) <= len(string):
            # print(pow(n,i)," ",binary)
            binary_array.append(binary)
        number += 1
    return binary_array


def check(binary_list):
    exist_string = []
    for i in binary_list:
        if search(string, i) is not None:
            exist_string.append(i)

    return exist_string


def find(string, binary_list):
    count = 0
    for i in binary_list:
        while search(string, i) is not None:
            count += str.count(i)
            string = string.replace(i, "")
            # print (i, count, str)

    return count


if __name__ == '__main__':
    string, string_len = read_from_file()
    print(string)
    print(string_len)
    result = power(string, string_len)

    result = check(result)
    result.reverse()
    # for i in result:
    #    print(i,' ',search(string, i))

    count = find(string, result)
    print(count)
