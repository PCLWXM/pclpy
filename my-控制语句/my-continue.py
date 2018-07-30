#要求输入员工的薪资，若薪资小于0 则重新输入。最后打印出录入员工的数量和
#薪资明细，以及平均薪资
empNum = 0
salarySum= 0
salarys = []
while True:
    s = input("请输入员工的薪资（按Q 或q 结束）:")
    if s.upper()=='Q':
        print("录入完成，退出")
        break
    if float(s)<0:
        continue
    empNum +=1
    salarys.append(float(s))
    salarySum += float(s)
print("员工数{0}".format(empNum))
print("录入薪资：",salarys)
print("平均薪资{0}".format(salarySum/empNum))