
class Head:
    def __init__(self):
        pass

class Hand:
    def __init__(self):
        pass

class Arm:
    def __init__(self, hand):
        self.hand = hand

class Feet:
    def __init__(self):
        pass

class Leg:
    def __init__(self, feet):
        self.feet = feet
class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg

class Human:
    def __init__(self, torso):
        self.torso = torso


Head1 = Head()
Right_Hand1 = Hand()
Left_Hand1 = Hand()
Right_Arm1 = Arm(Right_Hand1)
Left_Arm1 = Arm(Left_Hand1)
Right_Feet1 = Feet()
Left_Feet1 = Feet()
Right_Leg1 = Leg(Right_Feet1)
Left_Leg1 = Leg(Left_Feet1)
Torso1 = Torso(Head1, Right_Arm1, Left_Arm1, Right_Leg1, Left_Leg1)
Human1 = Human(Torso1)
