for x in(10, 20, 30):
    print(x*30)
print("*********************************")
for x in "abc":
    print(x)
print("*********************************")
d={"name":"carry","age":19,"job":"corder"}
for x in d:
    print(x)
print("-----------------------------------")
for x in d.keys():
    print(x)
print("-----------------------------------")
for x in d.values():
    print(x)
print("-----------------------------------")
for x in d.items():
    print(x)
print("***********************************")
for x in range(5):
    print(x)
print("-----------------------------------")
sum_all = 0
sum_odd = 0
sum_even = 0
for x in range(101):
    sum_all += x
    if x%2==1:
        sum_odd += x
    else:
        sum_even += x
print("1-100累加和:{0},奇数和:{1},偶数和:{2}".format(sum_all,sum_odd,sum_even))