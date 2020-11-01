def load_data(filename):
    with open(filename, 'r') as fp:
        lines = fp.readlines()
    content = []
    # 将十六进制串转为字符串
    for line in lines:
        h = int('0x' + line, 16)
        l = ''
        while h:
            l += chr(h & 0xff)
            h >>= 8
        content.append(l[::-1])
    return content

def dec(s, key):
    '''
    param s  : 待解码的字符串
    param key: 秘钥key
    '''
    ans = ''
    length = min(len(s), len(key))
    for i in range(length):
        ans += chr(ord(s[i]) ^ ord(key[i]))
    return ans

def decode(message, key):
    '''
    param message: 明文
    param key: 秘钥
    '''
    mes = []
    for line in message:
        m = dec(line, key)
        mes.append(m)
    print(mes)

if __name__ == "__main__":
    data = load_data('cr2-many-time-secrets/f331d71a103f49bc94c2cc7838c29a9c')
    print(data)
    decode(data, 'ALEXCTF{')
    # decode(data, 'Dear Friend')
    # decode(data, 'ALEXCTF{HERE')
    # decode(data, 'ncryption scheme')
    # decode(data, 'ALEXCTF{HERE_GOE')
    # decode(data, 'nderstood my mistake')
    # decode(data, 'ALEXCTF{HERE_GOES_TH')
    # # #decode(data, 'sed one time pad encode') 结果不对
    # decode(data, 'sed One time pad encrypt')
    # decode(data, 'ALEXCTF{HERE_GOES_THE_KE')
    # decode(data, ' proven to be not cracked')
    # decode(data, 'ALEXCTF{HERE_GOES_THE_KEY')
    # decode(data, 'sed One time pad encryption')
