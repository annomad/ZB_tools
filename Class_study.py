class Class_study():
    def __init__(self, val):
        self.name = val
        self.full_name = self.name + ' Lee'

    def aboutme(self):
        print('My name is :' + self.name)




class Bird(Class_study):
    # def __init__(self, c):
    #     pass    #如果初始化变量且没有链接，则丧失父类特性。
    def aboutme(self):
        print(self.full_name)

if __name__ == '__main__':
    mybird = Bird('jiu qiu')
    mybird.aboutme() #验证结果是：重写父类，不一定要用__init__方法。如果形参位置相同，则不用__init__方式传递
    print(mybird.name)
