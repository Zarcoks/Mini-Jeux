class Carte:
    def __init__(self, val, elt):
        self.elt = elt
        self.val = val
        self.symbol = ''
        self.color = ''
        self.look = []
        self.set_card()

    def set_card(self):
        #------------------------------------#
        if self.elt in ["pique", "trefle"]:
            self.color = "black"
        else:
            self.color = "red"
        #------------------------------------#

        dict_sym = {"1":'A',"11":'V',"12":'Q','13':'K'}
        if self.val == 1 or self.val > 10:
            self.symbol = dict_sym[str(self.val)]
        else:
            self.symbol = str(self.val)

        #---------------------------------------------------------------#
        #dico = {"trefle":'♣', "pique":'♤', "coeur":'♥', "carreau":'♦'}
        dico = {"trefle": '+', "pique": '^', "coeur": '#', "carreau": '/'}

        self.look.append("╔═══╗")
        if len(str(self.symbol)) < 2:
            self.look.append("║ "+str(self.symbol)+dico[self.elt]+"║")
        else:
            self.look.append("║" + str(self.symbol) + dico[self.elt] + "║")
        self.look.append("║   ║")
        self.look.append("╚═══╝")
        #---------------------------------------------------------------#

        if self.val == 1:
            self.val= 14


    def print_card(self):
        for elt in self.look:
            print(elt)

def print_some_cards(L, space):
    for i in range(4):
        for card in L:
            print(card.look[i], end=(' '*space))
        print()
"""
a = Carte(10, "coeur")
b = Carte(2, "trefle")
c = Carte(11, "coeur")
d = Carte(10, "coeur")
e = Carte(2, "pique")
f = Carte(11, "carreau")
a.print_some_cards([a, b, c, d, e, f])
TEST ZONE
"""