for x in range(5):
    for y in range(5):
        print (x,end="\t")
    print()
print("********************************")
for m in range(1,10):
    for n in range(1,10):
        print("{0}*{1}={2}".format(m,n,(m*n)),end="\t")
    print()
print("********************************")
for m in range(1,10):
    for n in range(1,m+1):
        print("{0}*{1}={2}".format(m,n,(m*n)),end="\t")
    print()
print("********************************")
#使用列表和字典存储表格的数据
r1 = dict(name="yi",age=18,salary=30000,city="bj")
r2 = dict(name="er",age=19,salary=20000,city="sh")
r3 = dict(name="sa",age=20,salary=10000,city="sz")
tb = [r1,r2,r3]
for x in tb:
    if x.get("salary")>15000:
        print(x)