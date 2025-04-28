from typing import Protocol, runtime_checkable

# 使用Python 3.8+的Protocol特性模拟接口
@runtime_checkable
class IMovable(Protocol):
    """可移动接口，定义了移动相关的方法
    
    使用Python的Protocol特性模拟C#中的接口
    @runtime_checkable装饰器允许在运行时使用isinstance检查
    """
    
    def move(self, distance: float) -> None:
        """移动指定距离"""
        ...
    
    def get_speed(self) -> float:
        """获取速度"""
        ...


# 传统方式模拟接口（适用于旧版Python）
class IFeedable:
    """可喂食接口，定义了喂食相关的方法
    
    使用传统类方式模拟C#中的接口
    """
    
    def feed(self, food: str) -> None:
        """喂食方法，需要被实现类重写"""
        raise NotImplementedError("子类必须实现feed方法")
    
    def is_hungry(self) -> bool:
        """检查是否饥饿，需要被实现类重写"""
        raise NotImplementedError("子类必须实现is_hungry方法")