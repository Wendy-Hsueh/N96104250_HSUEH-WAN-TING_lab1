import random
class Nine_Coins:
    def __init__(self, num):
        self._num = num
    #convert deccimal to binary
    def deccimalTObinary(self, num):
        self._a = "{0:b}".format(self._num)
        return self._a
    #(corresponds)convert binary to H,T
    def convertTOht(self,aa):
        self.ll=[]
        self.ll = list(str(aa))
        print('Nine_Coins: ', end='')
        for i in range(9):
            if(self.ll[i]=='0'):
                self.ll[i] = 'H'
            else:
                self.ll[i] = 'T' 
            print(self.ll[i],end='')
        i = i+1
    #all the coins will be flipped randomly
    def toss(self):
        #random coins
        random.shuffle(self.ll)
        print('-----After toss-----')
        print('Nine_Coins: ', end='')
        for i in range(9):
            print(self.ll[i],end='') 
        print()
        print('binary:',end='')
        result = 0
        for i in range(9):
            if(self.ll[i]=='H'):
                self.ll[i] = '0'
            else:
                self.ll[i] = '1' 
            print(self.ll[i],end='')
        #deccimal after flipped   
        for i in range(9):
            power = 2**(8-i)
            if self.ll[i] == '1':
                result += power
            else:
                result += 0
        i+=1
            
        print(' and decimal:', result)
        i = i+1
           
