unit_info = {
    "probe" :{
        "name":"프로브",
        "mineral":50,
        "gas":0,
        "hp":20,
        "shield":20,
        "damage":5
    },
     "zealot" :{
        "name":"질럿",
        "mineral":100,
        "gas":0,
        "hp":100,
        "shield":61,
        "damage":16
    },
     "dragoon" :{
        "name":"드라군",
        "mineral":125,
        "gas":50,
        "hp":100,
        "shield":80,
        "damage":20
    },
}

class Unit:
    # 속성: 이름, 체력, 방어막, 공격력
    def __init__(self, name, hp, shield, damage):
        self.name = name
        self.hp = hp
        self.shield = shield
        self.damage = damage
    

class Player:
    # 속성: 이름, 미네랄, 가스, 유닛리스트
    # 메소드: 유닛생산하기
    def __init__(self, nickname, mineral, gas, unitlist=[]):
        self.nickname = nickname
        self.mineral = mineral
        self.gas = gas
        self.unitlist = unitlist
    
    def produce(self, name, mineral, gas, hp, shield, damage):
        if self.mineral - mineral < 0:
            print("미네랄이 부족합니다.")
        elif self.gas - gas < 0:
            print("가스가 부족합니다.")
            self.mineral -= mineral
            self.gas -= gas
            unit= Unit(name, hp, shield, damage)
            self.unitlist.append(unit)
            print(f"[{name}]를 생산합니다.")


# 플레이어 생성
player1 = Player("Bisu", 400, 10)

# 유닛 생성
player1.produce(unit_info['probe']['name'], unit_info['probe']['mineral'], unit_info['probe']['gas'],
                unit_info['probe']['hp'], unit_info['probe']['shield'], unit_info['probe']['damage'])
player1.produce(unit_info['zealot']['name'], unit_info['zealot']['mineral'], unit_info['zealot']['gas'],
                unit_info['zealot']['hp'], unit_info['zealot']['shield'], unit_info['zealot']['damage'])
player1.produce(unit_info['dragoon']['name'], unit_info['dragoon']['mineral'], unit_info['dragoon']['gas'],
                unit_info['dragoon']['hp'], unit_info['dragoon']['shield'], unit_info['dragoon']['damage'])       

# 생성된 유닛
for unit in player1.unitlist:
    print("이름: [{}] 체력: [{}], 방어막 [{}], 데미지 [{}]".format(unit.name, unit.hp, unit.shield, unit.damage))
