

class Unit:

    count = 0
    def __init__(self, name, hp, shield, damage):
        self.name = name
        self.hp = hp
        self.shield = shield
        self.damage = damage
        Unit.count += 1
        print(f"[{self.name}]이(가) 생성 되었습니다.")

    def __str__(self):
        return f"[{self.name}] 체력 : {self.hp} 방어막 : {self.shield} 공격력 : {self.damage}"

    def hit(self, damage):
        if self.shield >= damage:
            self.shield -= damage
            damage = 0
        else:
            damage -= self.shield
            self.shield = 0
        
        if damage > 0:
            if self.hp > damage:
                self.hp -= damage
            else:
                self.hp = 0

    @classmethod # 클래스메소드
    def print_count(cls):
        print(f"생성된 유닛 개수 : [{cls.count}]")


class Math:# 정적메소드
    @staticmethod 
    def add(x,y):
        return x + y


probe = Unit("프로브", 20, 20, 5)
zealot = Unit("질럿", 100, 60, 16)
dragoon = Unit("드라군", 100, 80, 20)

Unit.print_count()  # 클래스 메소드 호출

print(Math.add(1,2)) # 정적 메소드 호출


