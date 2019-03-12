class FatherCls(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print('my father is %s, age is %s' %(self.name, self.age))
# 子类使用父类的初始化方法，第一种初始化方法
# class Son(FatherCls):
#
#     def __init__(self, name, age,hebby):
#         FatherCls.__init__(self,name, age)
#         self.hebby = hebby # 派生属性
#     def showMe(self):
#         print('my name is %s, age is %s, hebby is %s' %(self.name, self.age, self.hebby))
# 子类使用父类的初始化方法，第二种初始化方法
class Son(FatherCls):
    def __init__(self, name, age):
        super().__init__( name,age)
    def showMe(self):
        print('my name is %s, age is %s' %(self.name, self.age))
if __name__=='__main__':
    me = Son('xiaochao',22)
    me.showMe()