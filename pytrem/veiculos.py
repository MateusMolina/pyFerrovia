
from pytrem.equip import ACT, SysFreio

class carro:
    def __init__(self, id, massa, tipo):
       pass
   
class vagao(carro):
    def __init__(self, id, tipo, pEG, EGMAX,TB=0):
        self.id = id
        self.tipo = tipo
        self.TB = TB
        
        # Atributos Públicos
        self.m = 70*1000
        self.L = 12
        self.SysFreio = SysFreio(id, pEG, EGMAX)  
        self.ACT = ACT(0)
        self.pEG = pEG
        # Init dos Sistemas
        
    def __str__(self):
        return self.id
    
    @property
    def pEG(self):
        return self._pEG
    
    @pEG.setter
    def pEG(self, pEG):
        self._pEG = pEG
        self.SysFreio.pEG = pEG
    
    @property
    def a(self):
        FR, m = self.FR, self.m
        self._a = FR/m
        return self._a
    
    @property
    def FR(self):
        self._FR = self.FI + self.FE    
        return self._FR
    
    @property
    def FI(self):
        self._FI = self.SysFreio.FFren
        return self._FI
    
    @property
    def FE(self):
        return self._FE
    
    @FE.setter
    def FE(self, FE):
        self._FE = FE
