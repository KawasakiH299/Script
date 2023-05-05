import sys
args = sys.argv
print(args[1])
def add1(a,b):
    return a+b
#sys.argv的参数是字符串
resu = add1(int(sys.argv[1]),int(sys.argv[2]))
print(resu)
