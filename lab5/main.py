


def read_from_file():
    with open('graph.txt') as f:
        data = f.readline()
    data, n = data.split()
    return data, int(n)


def decToBinary(n):

    binary_list = [0] * n;
    i = 0;
    while (n > 0):
        binary_list[i] = n % 2;
        n = int(n / 2);
        i += 1;
    n =""
    for j in range(i - 1, -1,-1 ):
        #print(binary_list[j], end = "");
        n+=str(binary_list[j])
    return n

NO_OF_CHARS = 256


def bad_char_heuristic(string, size):
    bad_char = [-1] * NO_OF_CHARS
    for i in range(size):
        bad_char[ord(string[i])] = i;

    return bad_char


def search( txt, pat):
    m = len(pat)
    n = len(txt)
    bad_char = bad_char_heuristic(pat, m)
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1
        if j < 0:
            return s
            s += (m - bad_char[ord(txt[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - bad_char[ord(txt[s + j])])


def power(str, n):
    length= len(str)
    binary = ""
    i= 0
    binary_array=[]
    while len(binary)<=len(str):
        binary = decToBinary(pow(n,i))
        if len(binary)<=len(str):
            #print(pow(n,i)," ",binary)
            binary_array.append(binary)
        i+=1
    return binary_array

def check(result):
    strs = []
    for i in result:
        if search( string, i) is not None:
            strs.append(i)

    return strs

def find(str, list_binary):
    cstr= str
    list =list_binary
    count =0
    for i in list:
        while (search(str, i ) is not None):
            count+=str.count(i)
            str = str.replace(i, "")
            #print (i, count, str)

    return count

if __name__ == '__main__':
    string, n = read_from_file()
    print(string)
    print(n)
    result = power(string, n)

    result = check(result)
    result.reverse()
    #for i in result:
    #    print(i,' ',search(string, i))


    count = find(string, result)
    print(count)



