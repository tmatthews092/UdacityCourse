class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    if len(group.get_groups()):
        for g in group.get_groups():
            return is_user_in_group(user, g)
    return False


#Test One - Happy Path

group_1 = Group("group_1")
group_1.add_user("user_1")
group_1.add_user("user_2")
group_1.add_user("user_3")
group_2 = Group("group_2")
group_2.add_user("user_4")
group_2.add_user("user_5")
group_3 = Group("group_3")
group_3.add_user("user_6")
group_3.add_user("user_7")
group_3.add_group(group_2)
group_1.add_group(group_3)

assert is_user_in_group('user_4', group_1) == True
assert is_user_in_group('user_4', group_2) == True
assert is_user_in_group('user_4', group_3) == True

assert is_user_in_group('user_1', group_1) == True
assert is_user_in_group('user_1', group_2) == False
assert is_user_in_group('user_1', group_3) == False

assert is_user_in_group('user_7', group_1) == True
assert is_user_in_group('user_7', group_2) == False
assert is_user_in_group('user_7', group_3) == True

print('user_4 should be in group_1: ' + str(is_user_in_group('user_4', group_1))) #user_4 should be in group_1: True
print('user_4 should be in group_2: ' + str(is_user_in_group('user_4', group_2))) #user_4 should be in group_2: True
print('user_4 should be in group_3: ' + str(is_user_in_group('user_4', group_3))) #user_4 should be in group_3: True
print('user_1 should be in group_1: ' + str(is_user_in_group('user_1', group_1))) #user_1 should be in group_1: True
print('user_1 should be in group_2: ' + str(is_user_in_group('user_1', group_2))) #user_1 should be in group_2: False
print('user_1 should be in group_3: ' + str(is_user_in_group('user_1', group_3))) #user_1 should be in group_3: False
print('user_7 should be in group_1: ' + str(is_user_in_group('user_7', group_1))) #user_7 should be in group_1: True
print('user_7 should be in group_2: ' + str(is_user_in_group('user_7', group_2))) #user_7 should be in group_2: False
print('user_7 should be in group_3: ' + str(is_user_in_group('user_7', group_3))) #user_7 should be in group_3: True

#Test Two - Nulls or None existent user key

print('111111111 should be in group_1: ' + str(is_user_in_group('111111111', group_1))) #111111111 should be in group_1: False
print('None should be in group_1: ' + str(is_user_in_group(None, group_1))) #None should be in group_1: False
print('222222 should be in group_1: ' + str(is_user_in_group(222222, group_1))) #222222 should be in group_1: False

#Test Three - Extremely Nested User
g0 = Group("g0")
g1 = Group("g1")
g2 = Group("g2")
g3 = Group("g3")
g4 = Group("g4")
g5 = Group("g5")
g6 = Group("g6")
g7 = Group("g7")
g8 = Group("g8")
g9 = Group("g9")
g10 = Group("g10")
g11 = Group("g11")
g12 = Group("g12")
g13 = Group("g13")
g14 = Group("g14")
g15 = Group("g15")
g16 = Group("g16")
g17 = Group("g17")
g18 = Group("g18")
g19 = Group("g19")
g20 = Group("g20")
g1.add_group(g0)
g2.add_group(g1)
g3.add_group(g2)
g4.add_group(g3)
g5.add_group(g4)
g6.add_group(g5)
g7.add_group(g6)
g8.add_group(g7)
g9.add_group(g8)
g10.add_group(g9)
g11.add_group(g10)
g12.add_group(g11)
g13.add_group(g12)
g14.add_group(g13)
g15.add_group(g14)
g16.add_group(g15)
g17.add_group(g16)
g18.add_group(g17)
g19.add_group(g18)
g20.add_group(g19)
g0.add_user("deeplynesteduser")
print('deeplynesteduser should be in g20: ' + str(is_user_in_group('deeplynesteduser', g20))) #deeplynesteduser should be in g20: True
