#find 
import math

class RootEquation:
    def __init__(self,e) -> None:
        if self.simpleValidate(e)==True:
            print("---------------init----------")        
            self.getEquation(e)
            self.letCalculate()
        else:
            raise AssertionError("Your equations incorrect!")
         
    def simpleValidate(self,ev):
        vl:list=['^','x',"=",'+','-','0','1','2','3','4','5','6','7','8','9']
        e:list=list(ev)
        for i in e:
            if vl.__contains__(i)==False:
                return False   
        if ev.count('x')>2 or ev.count('^')>=2 or ev.count('=0')!=1 or ev.count("x^2")!=1: 
            return False
        return True
    
    def getEquation(self,e):
        #x^2+x+2=0
        el:list=e.split("x^2")
        el[0]=self.g(el[0])
        self.a=float(el[0])
        el1=el[1].split('x')
        el1[0]=self.g(el1[0])
        self.b=float(el1[0])
        el2=el1[1].split('=')
        self.c=float(el2[0])
        
    def delta(self):
        return self.b*self.b-4*self.a*self.c
    
    def letCalculate(self):
        if self.delta()>0:
            self.x1=str((-1*self.b+math.sqrt(self.delta()))/(2*self.a))
            self.x2=str((-1*self.b-math.sqrt(self.delta()))/(2*self.a))
            self.result="Result: x1="+self.x1+" , x2="+self.x2
        elif self.delta()==0:
            self.x1=str((-1*self.b+math.sqrt(self.delta()))/(2*self.a))
            self.x2=str(self.x1)
            self.result="Result: x1=x2="+self.x1
        else:
            self.x1="Not root 1"
            self.x2="Not root 2"
            self.result="No root "

    def g(self,v):
        if v=='' or v=='+':
            return "+1"
        elif v=='-':
            return "-1"
        else:
            return v
    
    def __str__(self):
        return self.result
    

k:object=RootEquation("2x^2+x-1=0")
print(k)

k:object=RootEquation("x^2+3x-2=0")
print(k)


