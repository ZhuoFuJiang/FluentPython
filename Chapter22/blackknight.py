# class BlackKnight:
#     def __init__(self):
#         self.members = ["an arm", 'anther arm',
#                         'a leg', 'another leg']
#         self.phrases = ["'Thi but a scratch.'", "It's just a flesh wound.",
#                         "I'm invincible!", "All right, we'll call it a draw."]
#
#     @property
#     def member(self):
#         print("next member is:")
#         return self.members[0]
#
#     @member.deleter
#     def member(self):
#         text = "BLACK KNIGHT (loses {})\n--{}"
#         print(text.format(self.members.pop(0), self.phrases.pop(0)))


class BlackKnight:
    def __init__(self):
        self.members = ["an arm", 'anther arm',
                        'a leg', 'another leg']
        self.phrases = ["'Thi but a scratch.'", "It's just a flesh wound.",
                        "I'm invincible!", "All right, we'll call it a draw."]

    def __getattr__(self, item):
        if item != 'member':
            # raise ValueError("obj {} has no {}".format(self, item))
            super(BlackKnight, self).__getattribute__(item)
        else:
            print("next member is:")
            return self.members[0]

    def __delattr__(self, item):
        if item != 'member':
            pass
        else:
            text = "BLACK KNIGHT (loses {})\n--{}"
            print(text.format(self.members.pop(0), self.phrases.pop(0)))


if __name__ == "__main__":
    knight = BlackKnight()
    print(knight.t)
    del knight.member
    print(knight.member)
    del knight.member
    print(knight.member)