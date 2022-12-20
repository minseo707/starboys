def maker(a, n):
    f=open('make.txt', 'w',encoding='utf8')
    f.write(a*n)
    f.close()
def faker(aa, n):
    ff=open('take.txt', "a", encoding='utf8')
    ff.write(aa*j)
    ff.close()
for i in range(5):
    t = maker('나비\n',i)
for j in range(5):
    tt = faker('호랑이\n',j)