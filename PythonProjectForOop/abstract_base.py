from abc import ABC, abstractmethod

# 抽象基类示例 - 类似于C#中的抽象类
class Animal(ABC):
    """Animal抽象基类，定义了所有动物都应该实现的方法
    
    在Python中使用abc模块实现抽象类，类似于C#中的abstract class
    """
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def make_sound(self):
        """发出声音的抽象方法，必须由子类实现
        
        类似于C#中的abstract方法
        """
        pass
    
    def describe(self):
        """描述动物的非抽象方法，可以被子类继承或重写
        
        类似于C#中的virtual方法
        """
        return f"这是一只{self.name}"