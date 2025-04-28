# 服务类，用于依赖注入示例
class SoundService:
    """声音服务类，用于生成动物的声音
    
    用于演示依赖注入模式，类似于C#中的服务注入
    """
    
    def __init__(self, volume: int = 5):
        self.volume = volume
    
    def make_animal_sound(self, sound: str) -> str:
        """根据音量生成动物声音"""
        # 根据音量调整声音的重复次数
        return sound * self.volume


class LoggingService:
    """日志服务类，用于记录动物行为
    
    用于演示依赖注入模式的另一个服务
    """
    
    def __init__(self, log_prefix: str = "[LOG]"): 
        self.log_prefix = log_prefix
        self.logs = []
    
    def log_action(self, message: str) -> None:
        """记录一条行为日志"""
        log_entry = f"{self.log_prefix} {message}"
        self.logs.append(log_entry)
        print(log_entry)
    
    def get_logs(self) -> list:
        """获取所有日志"""
        return self.logs