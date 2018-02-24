for every_letter in 'Hello world':
    print(every_letter)
for num in range(1,11):
    print(str(num)+'+1=',num+1)

songlist = ['Holy Diver','Thunderstruck','Rebel Reble']
for song in songlist:
    if song =='Holy Diver':
        print(song,'- Dio')
    elif song == 'Thunderstruck':
        print(song,'- AC/DC')
    elif song == 'Rebel Rebel':
        print(song, '- David Bowie')

for i in range(1,10):
    for j in range(1,10):
        print('{}x{}={}'.format(i,j,i*j))

count = 0
while True:
    print('Repeat this line !')#重复这一行
    count = count +1
    if count ==5:
        break

