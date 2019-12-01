import shelve
F = shelve.open('L200194051.data')
F['nama'] = ['Dafa Cahya Alfianiko']
F['nim'] = ['L200194051']
F['ttl'] = ['Surakarta, 19-05-2001']
F.close()
                
import shelve
F = shelve.open('L200194051.data')
print('nama: ', F['nama'][0])
print('nim: ', F['nim'][0])
print('tempat tanggal lahir: ', F['ttl'][0])
F.close()
