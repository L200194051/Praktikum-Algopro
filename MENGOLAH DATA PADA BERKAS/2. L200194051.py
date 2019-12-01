berkas=open('L200194051.txt','w')
berkas.write('L200194051\n')
berkas.write('Surakarta, 19-05-2001\n')
berkas.write('Dafa Cahya Alfianiko')
berkas.close()

for line in reversed (list(open('L200194051.txt'))):
    print(line.rstrip())
