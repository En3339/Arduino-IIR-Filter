class IIR2Filter:
    def __init__(self,_b0,_b1,_b2,_a0,_a1,_a2):
        self.a0 = _a0
        self.a1 = _a1
        self.a2 = _a2       
        self.b0 = _b0
        self.b1 = _b1
        self.b2 = _b2
        self.order1buffer=0
        self.order2buffer=0
        
    def filter(self,x):
        acc_input= x*self.a0 - self.order1buffer*self.a1 - self.order2buffer*self.a2
        acc_output= acc_input*self.b0 +  self.order1buffer*self.b1+self.order2buffer*self.b2
        self.order2buffer = self.order1buffer
        self.order1buffer = acc_input
        return acc_output