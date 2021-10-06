from abc import ABCMeta, abstractmethod


class Human(metaclass=ABCMeta):

    # 抽象メソッド 継承先クラスで実装の必要がある
    @abstractmethod
    def attack(self):
        pass

    # 共通のメソッド
    def defend(self) -> str:
        return "防御"


class Saber(Human):
    def attack(self) -> str:
        return "剣で攻撃"


class Archer(Human):
    def attack(self) -> str:
        return "弓で攻撃"


class Caster(Human):
    def attack(self) -> str:
        return "魔法で攻撃"


saver = Saber()
print(saver.attack())  # 剣で攻撃

archer = Archer()
print(archer.attack())  # 弓で攻撃

caster = Caster()
print(caster.attack())  # 魔法で攻撃
print(caster.defend())  # 防御
