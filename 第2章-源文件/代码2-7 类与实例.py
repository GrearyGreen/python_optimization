# 定义一个类
class cat():
    # 初始化函数，通常类也是在这报错，因为实例化时传参的原因
    # 是构造函数
    # self是传输实例对象在内存中的一个地址
    # 函数和方法的区别：在类中叫函数，在实例中称为方法
    # 类中的参数叫属性
    def __init__(self, color, weight):
        # 需要两个参数传入：color,weight
        # self是默认的，指向自己
        self.color = color
        self.weight = weight

    def catch_mice(self):
        """抓老鼠的方法"""
        print('抓老鼠')

    def eat_mice(self):
        """吃老鼠"""
        print('吃老鼠')


# 类的实例化
my_cat = cat('yello', 10)

# 调用类的方法
my_cat.catch_mice()
# 输出 抓老鼠

my_cat.eat_mice()
# 输出 吃老鼠

# 查看类的属性
print(my_cat.color)
# 输出 yello

print(my_cat.weight)
# 输出 10
