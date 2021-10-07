import random
class food:
    def __init__(self, avoid={}):
        self.avoid = avoid
        self.p = random.randint(0,30)
        self.q = 2*random.randint(0,40)
        n = True
        while(n):
            try:
                if avoid[str(self.p)+','+str(self.q)]:
                    self.p = random.randint(0,30)
                    self.q = 2*random.randint(0,40)
            except:
                n = False
