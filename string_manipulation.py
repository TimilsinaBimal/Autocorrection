class Manipulation():
    def __init__(self, word):
        self.word = word
        self.letters = 'abcdefghijklmnopqrstuvwxyz'
        self.split_l = [
            (self.word[:i], self.word[i:])
            for i in range(len(self.word)+1)
        ]

    def delete_letter(self):
        delete_l = [L[:]+R[1:] for L, R in self.split_l if R]
        return delete_l

    def switch_letter(self):
        switch_l = [L[:-1]+R[0]+L[-1]+R[1:]
                    for L, R in self.split_l if L and R]
        return switch_l

    def replace_letter(self):
        replace_l = sorted(
            list({
                L + letter + R[1:]
                for letter in self.letters
                for L, R in self.split_l if R
            }))
        try:
            replace_l.remove(self.word)
        except:
            pass
        return replace_l

    def insert_letter(self):
        insert_l = [
            L + letter + R
            for letter in self.letters
            for L, R in self.split_l
        ]
        return insert_l
