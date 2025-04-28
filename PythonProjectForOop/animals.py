from abstract_base import Animal
from interfaces import IMovable, IFeedable
from services import SoundService, LoggingService

# 具体动物类实现
class Dog(Animal, IFeedable):
    """狗类，继承自Animal抽象基类，实现IFeedable接口
    
    展示继承、接口实现和依赖注入
    """
    
    def __init__(self, name: str, breed: str, sound_service: SoundService = None, logging_service: LoggingService = None):
        """构造函数，展示依赖注入模式
        
        Args:
            name: 狗的名字
            breed: 狗的品种
            sound_service: 注入的声音服务（依赖注入）
            logging_service: 注入的日志服务（依赖注入）
        """
        super().__init__(name)
        self.breed = breed
        self.hunger_level = 5  # 0-10表示饥饿程度
        
        # 依赖注入 - 类似于C#中的构造函数注入
        self.sound_service = sound_service if sound_service else SoundService()
        self.logging_service = logging_service
    
    def make_sound(self) -> str:
        """实现抽象方法，展示方法重写
        
        类似于C#中的override方法
        """
        sound = "汪!"
        if self.logging_service:
            self.logging_service.log_action(f"{self.name}正在叫")
        return self.sound_service.make_animal_sound(sound)
    
    def describe(self) -> str:
        """重写基类的方法，展示方法重写
        
        类似于C#中的override方法
        """
        return f"这是一只{self.breed}品种的狗，名叫{self.name}"
    
    # 实现IFeedable接口方法
    def feed(self, food: str) -> None:
        """实现接口方法"""
        self.hunger_level = max(0, self.hunger_level - 3)
        if self.logging_service:
            self.logging_service.log_action(f"{self.name}吃了{food}，饥饿度降低到{self.hunger_level}")
    
    def is_hungry(self) -> bool:
        """实现接口方法"""
        return self.hunger_level > 3
    
    # 方法重载模拟 - 通过默认参数和可变参数
    def play(self, activity: str = "接飞盘", *toys) -> str:
        """模拟方法重载
        
        Python不直接支持方法重载，但可以通过默认参数和可变参数模拟
        类似于C#中的方法重载
        
        Args:
            activity: 玩耍的活动
            *toys: 可变数量的玩具
        """
        if not toys:
            return f"{self.name}正在{activity}"
        elif len(toys) == 1:
            return f"{self.name}正在用{toys[0]}玩{activity}"
        else:
            toy_list = ", ".join(toys)
            return f"{self.name}正在用{toy_list}玩{activity}"


class Cat(Animal, IMovable, IFeedable):
    """猫类，继承自Animal抽象基类，实现IMovable和IFeedable接口
    
    展示多重接口实现和依赖注入
    """
    
    def __init__(self, name: str, color: str, sound_service: SoundService = None, logging_service: LoggingService = None):
        """构造函数，展示依赖注入模式"""
        super().__init__(name)
        self.color = color
        self.speed = 10.0  # 默认速度
        self.hunger_level = 5  # 0-10表示饥饿程度
        
        # 依赖注入 - 类似于C#中的构造函数注入
        self.sound_service = sound_service if sound_service else SoundService(volume=2)
        self.logging_service = logging_service
    
    def make_sound(self) -> str:
        """实现抽象方法"""
        sound = "喵~"
        if self.logging_service:
            self.logging_service.log_action(f"{self.name}正在叫")
        return self.sound_service.make_animal_sound(sound)
    
    def describe(self) -> str:
        """重写基类的方法"""
        return f"这是一只{self.color}颜色的猫，名叫{self.name}"
    
    # 实现IMovable接口方法
    def move(self, distance: float) -> None:
        """实现接口方法"""
        if self.logging_service:
            self.logging_service.log_action(f"{self.name}移动了{distance}米")
        # 移动会增加饥饿感
        self.hunger_level = min(10, self.hunger_level + distance/10)
    
    def get_speed(self) -> float:
        """实现接口方法"""
        # 饥饿会影响速度
        return self.speed * (1 - self.hunger_level/20)
    
    # 实现IFeedable接口方法
    def feed(self, food: str) -> None:
        """实现接口方法"""
        self.hunger_level = max(0, self.hunger_level - 2)
        if self.logging_service:
            self.logging_service.log_action(f"{self.name}吃了{food}，饥饿度降低到{self.hunger_level}")
    
    def is_hungry(self) -> bool:
        """实现接口方法"""
        return self.hunger_level > 2