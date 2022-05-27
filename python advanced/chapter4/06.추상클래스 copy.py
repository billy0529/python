from abc import * # 추상 클래스 사용을 위해 임포트

class Item(metaclass=ABCMeta): # 추상 클래스 사용하겠다.
    
    def __init__(self, name):
        self.name = name
    
    def pick(self):
        print(f"[{self.name}] 을(를) 주웠습니다.")

    def discard(self):
        print(f"[{self.name}] 을(를) 버렸습니다.")

    @abstractmethod # 추상 클래스에 메소드 적용. 상속자가 반드시 해당 메소드를 구현해야함
    def use(self):
        pass


class Weapon(Item):

    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage

    def use(self):
        print(f"[{self.name}]을(를) 이용해 {self.damage}로 공격합니다.")


class HealingItem(Item):

    def __init__(self, name, recovery_amount):
        super().__init__(name)
        self.recovery_amount = recovery_amount

    def use(self):
        print(f"[{self.name}]을(를) 사용합니다. {self.recovery_amount} 회복") 


m16 = Weapon("m16", 110)
bandage = HealingItem("붕대", 20)

m16.use()
bandage.use()



