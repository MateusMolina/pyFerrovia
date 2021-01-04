
class SysFreio:
    
    def __init__(self, id, pEG, EGMAX):  
        self.id = id
        self.EGMAX = EGMAX
        self.pEG = pEG
        # Atributos Privados
        self._A = 0.1
        self._R = 0.2
        self._E = 3
        
           
    # Sensor de CF
    @property
    def pCF(self):
        pEG = self.pEG
        Fator = 2.5
        self._pCF = Fator * (self.EGMAX - pEG)
        return self._pCF
        
    # Sensor de EG
    @property
    def pEG(self):
        return self._pEG
    
    @pEG.setter
    def pEG(self, P=110):
        self._pEG = P
        return self._pEG
    
    @property
    def FFren(self):
        P, A, R, E = self.pCF, self._A, self._R, self._E
        self._FFren = P * A * R * E * 10
        return self._FFren
    
class ACT:
    def __init__(self, tipo):
        # Pars iniciais
        self._k = 70000000
        self._c = 60000000
    
    def k(self, x):
        return self._k
    
    def c(self, x):
        return self._c
    
    