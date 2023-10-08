import math

def waveControll(val1 , val2):
    waveEq1:bool=waveValidateInput(val1)
    waveEq2:bool=waveValidateInput(val2)
    if waveEq1==True and waveEq2==True:
        return True
    else:
        return False
      
def waveValidateInput(val1:str):
    value1=val1.strip().lower().replace(' ','')
    validateList:list=['s','i','n','sin','0','1','2','3','4','5','6','7','8','9','(',')','t','/','+','-','π']
    valueEquation:list=value1
    vEq1:bool=False
    vEq2:bool=False
    vEq3:bool=False
  
    for v in valueEquation:
        if validateList.__contains__(v):
            vEq1=True
        else:
            print('False Step 1')
            return False 
        
    indexOfn:int=valueEquation.index('n')
    if valueEquation[indexOfn+1]!="(":
        print('False step 2')
        return False
    else:
        vEq2=True
        
    indexOfend:int=len(valueEquation)
    if valueEquation.index(')')!=(indexOfend-1):
        print('False Step 3')
        return False
    else :
        vEq3=True            
    if value1.count('+')<=1 and value1.count('-')<=1 and value1.count('(')==1 and value1.count(')')==1 and value1.count('sin')==1 and value1.count('t')==1 and value1.count('/')<=1 and value1.count('s')==1 and value1.count('i')==1 and value1.count('n')==1 and value1.count('π')<=2 and vEq1==True and vEq2==True and vEq3==True :
        return True
    else:
        print('False step 4')
        return False                            
    return False


class MWave:
    def __init__(self, waveEquation: str):
        # wavelist: list = list(waveEquation.lower().strip())
        # print(waveEquation)
        # sv: list = ['(', ')', 's', 'i', 'n', 't']
        # if wavelist.__contains__(sv[0]) and wavelist.__contains__(sv[1]) and wavelist.__contains__(
        #         sv[2]) and wavelist.__contains__(sv[3]) and wavelist.__contains__(sv[4]) and wavelist.__contains__(
        #         sv[5]) and waveEquation.__contains__('sin') and wavelist.count('s') == 1 and wavelist.count('i') == 1 and wavelist.count('n') == 1:
        #     self.wavestatus = True
        #     print('init : ' + str(self.wavestatus))
        #     self.waveEquation = waveEquation.lower().strip()
        if waveValidateInput(waveEquation)==True:
            self.wavestatus = True
            print('init : ' + str(self.wavestatus))
            self.waveEquation = waveEquation.lower().strip()
        else:
            self.wavestatus = False
            self.waveEquation = ''
            print('fail init : ' + str(self.wavestatus))
        if len(self.waveEquation) > 0:
            wavetwo: list = self.waveEquation.split('s')
            if len(wavetwo) > 2:
                return
            self.amplitude = wavetwo[0]
            wavepart2: str = wavetwo[1]
            waw = wavepart2.split('(')[1]  # result: 100t+phase)

            self.w = (waw.split('t')[0]).replace(' ', '')  # result 100
            
            if wavepart2.__contains__('+') or wavepart2.__contains__('-'):
                wphase = waw.split('t')[1]
                if len(wphase.replace(' ', '')) > 2:
                    self.phase = wphase.replace(')', '')
                else:
                    self.phase = '0'
            else:
                self.phase = '0'
        else:
            return

    def getAmplitude(self):
        return self.amplitude
    
    def setAmplitude(self, amplitude: str):
        self.amplitude = amplitude

    def getW(self):
        return self.w

    def setW(self, w):
        self.w = w

    def getPhase_Radian(self):
        self.phase0=self.phase
        if self.phase0.__contains__('π') :
            mypi = '*' + str(math.pi)
            print(mypi)
            self.phase0 = self.phase0.replace('π', mypi)
            if self.phase0.startswith('+*') or self.phase0.startswith('-*'):
                self.phase0=self.phase0.replace('*','')    
        return eval(self.phase0)

    def setPhase(self, phase):
        self.phase = phase
        
    def getPhase(self):
        return self.phase
    
    def getphaseDegree(self):
        #pi=180
        self.phase0=self.phase
        
        # if self.phase0.__contains__('1π'):
        #     self.phase0=self.phase0.replace('π',str(math.pi))
        #     return eval(self.phase0)
        if self.phase0.__contains__('π') :
            mypi = '*180'
            self.phase0 = self.phase0.replace('π', mypi)
            if self.phase0.startswith('+*') or self.phase0.startswith('-*'):
                self.phase0=self.phase0.replace('*','')    
        return eval(self.phase0)

    def __str__(self):
        return self.amplitude + " " + self.w + " " + self.phase

def writePhase(phase):
    if phase.__contains__('+'):
        return phase.replace('+','')
    return phase 


# t1='100sin(10 πt+2/3)'
# t2='200sin(10 πt+1/3)'
# y1=MWave(t1)
# y2=MWave(t2)
# print(y1.amplitude)
# print(y1.w)
# print(y1.phase)
# print(y1.getPhase_Radian())

#convert Degree to Radian Style
def simplyP(xd):
    x=math.gcd(int(xd),180)
    r:str=str(int(xd/x))
    d:str=str(int(180/x))
    return r+"π/"+d



class SumWave:
    def __init__(self,wEq1,wEq2):
        if MWave(wEq1).w==MWave(wEq2).w:
            self.wave1=MWave(wEq1)
            self.wave2=MWave(wEq2)
        else:
            print("User input wrong")

    def sumAmplituteWithoutSquare(self):
        return math.pow(self.sumAmpCos(),2)+math.pow(self.sumAmpSin(),2)
    def sumAmpTotal(self):
        return math.sqrt(self.sumAmplituteWithoutSquare())
    
    def sumAmpSin(self):
        a1:float=float(self.wave1.amplitude)
        sinPhi1:float=math.sin(float(self.wave1.getPhase_Radian()))
        a2:float=float(self.wave2.amplitude)
        sinPhi2:float=math.sin(float(self.wave2.getPhase_Radian()))
        return  a1*sinPhi1+a2*sinPhi2
    def sumAmpCos(self):
        a1:float=float(self.wave1.amplitude)
        cosPhi1:float=math.cos(float(self.wave1.getPhase_Radian()))
        a2:float=float(self.wave2.amplitude)
        cosPhi2:float=math.cos(float(self.wave2.getPhase_Radian()))
        return a1*cosPhi1+a2*cosPhi2

    def tanPhiRadian(self):
        return abs(self.sumAmpCos()/self.sumAmpSin())
    
    def tanPhiDegree(self):
        return math.degrees(math.atan(self.tanPhiRadian()))

    def simplyDegreeToRadianStyle(self)->str:
        x=math.gcd(int(self.tanPhiDegree()),180)
        r:str=str(int(self.tanPhiDegree()/x))
        d:str=str(int(180/x))
        return r+"π/"+d

    def tanSimply(self):
        tx=int(math.degrees(math.atan(self.tanPhiRadian())))
        ax=self.sumAmpCos()
        ay=self.sumAmpSin()
        if ax>0 and ay>0:
            return self.simplyDegreeToRadianStyle()
        
        elif ax<0 and ay>0:
            val=180-tx
            return simplyP(val)
        elif ax<0 and ay<0:
            val=180+tx
            t=simplyP(val)
            return t
        elif ax>0 and ay<0:
            return '-'+self.simplyDegreeToRadianStyle()
        else:
            return "can not process!"

    def __str__(self):
        # return self.wave1.__str__() + ' ' + self.wave2.__str__()
        self.bphase=self.tanSimply()
        if self.tanSimply().__contains__('-')==False:
            self.bphase="+"+self.tanSimply()
        return "Y="+str(round(self.sumAmpTotal(),4))+"sin("+self.wave1.w+"t "+self.bphase+")"
    
# t1: str = '100sin(10 πt+0.5)'
# t2: str = '200sin(10 πt+0.5)'
# y1 = MWave(t1)
# y2 = MWave(t2)
# s = SumWave("100sin(10 πt+2/3)","100sin(140 πt+2/3)")
# print(s.buildSumWave())


def nd():
    m_sin:list=[]
    m_cos:list=[]
    m_tan:list=[]
    

    return ""
class writePhaseMath:
    def __init__(self,w):
        if w.__contains__('/'): 
            self.wP10=w.split('/')[0]
            self.wP11=w.split('/')[1]
            self.wPnumber=2
        else:
            self.wP10=w
            self.wP11=""
            self.wPnumber=1
    def __str__(self):
        return self.wP10+" "+self.wP11 +" "+str(self.wPnumber)
    
class writePhaseMathSpecial:
    def __init__(self,w):
        if w.__contains__('/'): 
            self.wP10=w.split('/')[0]
            
            if self.wP10.__contains__('-'):
                self.wP10=self.wP10.replace('-','')
                self.sign="-"
                self.sign1="-"
                
                
            else:
                self.sign="+"
                self.sign1=""
            self.wP11=w.split('/')[1]
            self.wPnumber=2
        else:        
            self.sign=''
            self.wP10=w
            self.wP11=""
            self.wPnumber=1
    def __str__(self):
        return self.wP10+" "+self.wP11 +" "+str(self.wPnumber)
    
   