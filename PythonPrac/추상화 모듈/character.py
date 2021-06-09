# character.py
from abc import * # Abstrace Base Class

class Character(metaclass = ABCMeta):
  def __init__(self):
    self.hp = 100
    self.attack_power = 20

  def attack(self, other, attack_kind):
    other.get_damage(self.attack_power, attack_kind)

  @abstractmethod # Character 클래스를 상속받는 모든 클래스는 하기 함수를 오버라이딩으로 구현해야 인스턴스 생성이 가능하다.  
  def get_damage(self, attack_power, attack_kind):
    pass

# 테스트코드    
if __name__ == '__main__':
    ch1 = Character()  # TypeError 발생 (Can't instantiate abstract class Character with abstract methods get_damage)