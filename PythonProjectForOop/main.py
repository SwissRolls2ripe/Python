#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
面向对象编程示例 - 展示Python中模拟C#的OOP特性

本示例展示了如何在Python中实现以下面向对象编程特性：
1. 抽象类和抽象方法（使用abc模块）
2. 接口模拟（使用Protocol和传统类）
3. 依赖注入（通过构造函数注入）
4. 封装（通过访问修饰符和属性）
5. 继承（类继承）
6. 多态（通过基类引用调用派生类方法）
7. 方法重载模拟（通过默认参数和可变参数）
8. 方法重写（覆盖基类方法）
"""

from abstract_base import Animal
from interfaces import IMovable, IFeedable
from services import SoundService, LoggingService
from animals import Dog, Cat
from typing import List, cast
import inspect


def demonstrate_polymorphism(animals: List[Animal]) -> None:
    """展示多态性
    
    通过基类引用调用派生类方法，展示多态性
    类似于C#中的多态
    """
    print("\n===== 多态性演示 =====")
    for animal in animals:
        print(f"动物：{animal.name}")
        print(f"描述：{animal.describe()}")
        print(f"声音：{animal.make_sound()}")
        print("---")


def demonstrate_interfaces(movable: IMovable, feedable: IFeedable) -> None:
    """展示接口使用
    
    通过接口引用调用实现类方法，展示接口的使用
    类似于C#中的接口使用
    """
    print("\n===== 接口演示 =====")
    # 使用IMovable接口
    print(f"移动前速度：{movable.get_speed():.2f}")
    movable.move(5.0)
    print(f"移动后速度：{movable.get_speed():.2f}")
    
    # 使用IFeedable接口
    print(f"喂食前是否饥饿：{feedable.is_hungry()}")
    feedable.feed("美味食物")
    print(f"喂食后是否饥饿：{feedable.is_hungry()}")


def demonstrate_method_overloading(dog: Dog) -> None:
    """展示方法重载模拟
    
    通过默认参数和可变参数模拟方法重载
    类似于C#中的方法重载
    """
    print("\n===== 方法重载模拟 =====")
    print(dog.play())  # 使用默认参数
    print(dog.play("追球"))  # 覆盖默认参数
    print(dog.play("玩耍", "球"))  # 使用一个额外参数
    print(dog.play("玩耍", "球", "绳子", "飞盘"))  # 使用多个额外参数


def demonstrate_dependency_injection() -> None:
    """展示依赖注入
    
    通过构造函数注入不同的服务实例
    类似于C#中的依赖注入
    """
    print("\n===== 依赖注入演示 =====")
    # 创建服务实例
    quiet_service = SoundService(volume=1)
    loud_service = SoundService(volume=10)
    logging_service = LoggingService(log_prefix="[动物行为]")
    
    # 注入不同的服务
    quiet_dog = Dog("小静", "哈士奇", sound_service=quiet_service, logging_service=logging_service)
    loud_dog = Dog("大声", "德牧", sound_service=loud_service, logging_service=logging_service)
    
    print(f"安静的狗：{quiet_dog.make_sound()}")
    print(f"吵闹的狗：{loud_dog.make_sound()}")
    print("\n日志记录：")
    for log in logging_service.get_logs():
        print(f"  {log}")


def demonstrate_runtime_type_checking() -> None:
    """展示运行时类型检查
    
    使用isinstance检查对象是否实现了特定接口
    类似于C#中的is和as操作符
    """
    print("\n===== 运行时类型检查 =====")
    dog = Dog("旺财", "金毛")
    cat = Cat("咪咪", "橘色")
    
    # 检查对象是否是某个类的实例
    print(f"dog是Animal的实例：{isinstance(dog, Animal)}")
    print(f"cat是Animal的实例：{isinstance(cat, Animal)}")
    
    # 检查对象是否实现了某个接口
    print(f"dog实现了IMovable接口：{isinstance(dog, IMovable)}")
    print(f"cat实现了IMovable接口：{isinstance(cat, IMovable)}")
    print(f"dog实现了IFeedable接口：{isinstance(dog, IFeedable)}")
    print(f"cat实现了IFeedable接口：{isinstance(cat, IFeedable)}")


def main() -> None:
    """主函数，运行所有演示"""
    print("Python面向对象编程示例 - 模拟C#的OOP特性\n")
    
    # 创建动物实例
    dog = Dog("旺财", "金毛")
    cat = Cat("咪咪", "橘色")
    
    # 展示多态性
    animals = [dog, cat]
    demonstrate_polymorphism(animals)
    
    # 展示接口使用
    # 注意：我们需要使用cast来告诉类型检查器cat实现了IMovable接口
    # 这只是为了类型检查，运行时不需要
    demonstrate_interfaces(cast(IMovable, cat), dog)
    
    # 展示方法重载模拟
    demonstrate_method_overloading(dog)
    
    # 展示依赖注入
    demonstrate_dependency_injection()
    
    # 展示运行时类型检查
    demonstrate_runtime_type_checking()


if __name__ == "__main__":
    main()