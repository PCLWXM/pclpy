#员工一共4 人。录入这4 位员工的薪资。全部录入后，打印提示“您已经全部录
#入4 名员工的薪资”。最后，打印输出录入的薪资和平均薪资

salarySum= 0
salarys = []
for i in range(4):
    s = input("请输入一共4 名员工的薪资（按Q 或q 中途结束）:")
    if s.upper()=='Q':
        print("录入完成，退出")
        break
    if float(s)<0:
        continue
    salarys.append(float(s))
    salarySum += float(s)
else:
    print("您已经全部录入4 名员工的薪资")
print("录入薪资：",salarys)
print("平均薪资{0}".format(salarySum/4))