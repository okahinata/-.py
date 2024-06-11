'''
学籍番号：F222014
氏名：岡 日那汰
'''

# 抽象メソッド・型ヒント・特殊メソッド

from abc import ABC,abstractmethod
import math
class Shape(ABC):
    def __init__ (self,name:str):
        self.name=name
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        return self.name+'の面積：'+str(self.area())+'、周囲の長さ'+str(self.perimeter())
    
class Rectangle(Shape):
    def __init__(self,width:float,height:float):
        super().__init__('長方形')
        self.width=width
        self.height=height

    def area(self)->float:
        return self.width*self.height
    
    def perimeter(self)->float:
        return 2*(self.width+self.height)
class Circle(Shape):
    def __init__ (self,radius:float):
        super().__init__('円')
        self.radius=radius

    def area(self)->float:
        return math.pi*self.radius*self.radius
    
    def perimeter(self)->float:
        return 2*math.pi*self.radius
    
if __name__ == '__main__':
    rectangle = Rectangle(5.0, 3.0)
    circle = Circle(4.0)
    print(rectangle)
    print(circle)

#出力結果
'''
長方形の面積：15.0、周囲の長さ16.0
円の面積：50.26548245743669、周囲の長さ25.132741228718345
'''