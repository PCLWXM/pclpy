class Student:
    def __init__(self,name,score):   #self必须位于第一个参数
        self.name = name
        self.score = score

    def say_score(self):   #self必须位于第一个参数
        print("{0}的分数是：{1}".format(self.name,self.score))

s1 = Student("gaoyi",89)    #通过类名（）调用构造函数
s1.say_score()

s1.age = 33
s1.salary = 4000
print(s1.salary)
print(s1.salary)
print(s1.salary)
print(s1.salary)
print(s1.salary)