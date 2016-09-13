s = '\r\n'
res = ''
for i in s:
    res += '{: 02X}'.format(ord(i))
print(res)