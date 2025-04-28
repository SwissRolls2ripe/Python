# Python面向对象编程示例

本项目展示了如何在Python中实现类似C#的面向对象编程特性，包括抽象类、接口模拟、依赖注入、封装、继承、多态、方法重载和方法重写。

## 项目结构

- `abstract_base.py`: 定义抽象基类Animal，使用abc模块实现抽象方法
- `interfaces.py`: 使用Protocol和传统类方式模拟接口（IMovable和IFeedable）
- `services.py`: 定义服务类（SoundService和LoggingService）用于依赖注入
- `animals.py`: 实现具体的动物类（Dog和Cat），展示继承、多态和接口实现
- `main.py`: 主程序，展示所有面向对象编程特性的使用

## 实现的面向对象编程特性

### 1. 抽象类和抽象方法

使用Python的`abc`模块定义抽象基类`Animal`和抽象方法`make_sound()`，强制子类实现这些方法。

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
```

### 2. 接口模拟

使用Python 3.8+的`Protocol`特性和传统类方式模拟接口。

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class IMovable(Protocol):
    def move(self, distance: float) -> None: ...
    def get_speed(self) -> float: ...
```

### 3. 依赖注入

通过构造函数注入服务实例，实现依赖注入模式。

```python
def __init__(self, name: str, breed: str, sound_service: SoundService = None, logging_service: LoggingService = None):
    # 依赖注入 - 类似于C#中的构造函数注入
    self.sound_service = sound_service if sound_service else SoundService()
    self.logging_service = logging_service
```

### 4. 封装

通过类的属性和方法实现封装，控制对数据的访问。

### 5. 继承

通过类继承实现代码复用，`Dog`和`Cat`类继承自`Animal`抽象基类。

```python
class Dog(Animal, IFeedable):
    # 实现代码...

class Cat(Animal, IMovable, IFeedable):
    # 实现代码...
```

### 6. 多态

通过基类引用调用派生类方法，实现多态性。

```python
def demonstrate_polymorphism(animals: List[Animal]) -> None:
    for animal in animals:
        print(animal.make_sound())  # 调用具体实现类的方法
```

### 7. 方法重载模拟

Python不直接支持方法重载，但可以通过默认参数和可变参数模拟。

```python
def play(self, activity: str = "接飞盘", *toys) -> str:
    # 根据参数数量不同，实现不同的行为
```

### 8. 方法重写

子类重写父类的方法，实现不同的行为。

```python
def describe(self) -> str:
    # 重写基类的方法
    return f"这是一只{self.breed}品种的狗，名叫{self.name}"
```

## 运行示例

```bash
python main.py
```

运行后，将展示各种面向对象编程特性的实现和使用。