import random
from time import sleep


class Character:
    """
    모든 캐릭터의 모체가 되는 클래스
    """

    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


# 1.캐릭터생성
class Player(Character):
    def __init__(self, name, hp, mp, power):
        self.mp = mp
        super().__init__(name, hp, power)

    def magic_attack(self, other):
        damage = random.randint(self.power - 1, self.power + 3)
        print(f"{self.name}의 마법공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")


print("**게임에 접속하신 것을 환영합니다.")
print('캐릭터를 생성 하시겠습니까? (1.네, 2.아니오)')
choice = input()
if choice == '1':
    name = input("ID를 입력해주세요. : ")

# 2. 스텟 부여 (랜덤으로)
    while 1:
        power = 10
        hp = random.randrange(40, 45)
        mp = random.randrange(20, 25)
        print(f'\npower:{power}, mp:{mp}, hp:{hp}')
        print("\n 해당 캐릭터로 게임을 시작하시겠습니까? (1.네 2.아니오)")
        choice2 = input()
        if choice2 == '2':
            continue
        elif choice2 == '1':
            user = Player(name, hp, mp, power)
            sleep(1)
            print("\n 결정되었습니다.")
            print(f"""
                  name = {user.name}
                  power = {user.power}
                  HP = {user.hp}
                  MP = {user.mp}""")
            break

elif choice == '2':
    print("게임을 종료하겠습니다.")


#     # 3.몬스터 생성


class Monster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)


monster = Monster("몬스터1", 30, 10)
player = Player(name, hp, mp, power)


# 4.배틀
while 1:
    # show_status로 플레이어와 몬스터의 상태 정보 출력
    sleep(2)
    print("---------------턴 시작---------------")
    player.show_status()
    monster.show_status()

    sleep(2)
    print('-------------플레이어 턴--------------')
    sleep(1)
    # 5.일반공격/마법공격 선택
    print('\n어떤 공격을 하시겠습니까? 1.일반공격 2.마법공격')
    action = input()

    if action == "exit":
        break
    elif action == '1':
        player.attack(monster)

    elif action == '2':
        player.magic_attack(monster)
    else:
        print('잘못 입력하셨습니다.')
        continue

    if monster.hp <= 0:
        print(f'{name}이 승리하셨습니다.')
        break
    else:
        print(f'{name}이 패배하였습니다.')
        break
        # 6_1. 승리

        # 6_2. 패배
