# character.py
from abc import * # Abstrace Base Class

class Character(metaclass = ABCMeta):
  def __init__(self):
    self.hp = 100
    self.attack_power = 20

  def attack(self, other, attack_kind):
    other.get_damage(self.attack_power, attack_kind)

  @abstractmethod # Character Ŭ������ ��ӹ޴� ��� Ŭ������ �ϱ� �Լ��� �������̵����� �����ؾ� �ν��Ͻ� ������ �����ϴ�.  
  def get_damage(self, attack_power, attack_kind):
    pass

# �׽�Ʈ�ڵ�    
if __name__ == '__main__':
    ch1 = Character()  # TypeError �߻� (Can't instantiate abstract class Character with abstract methods get_damage)