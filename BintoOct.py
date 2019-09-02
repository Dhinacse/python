binary = input()
if binary == 'x':
    exit();
else:
    temp = int(binary, 2);
    print(oct(temp)[2:])
