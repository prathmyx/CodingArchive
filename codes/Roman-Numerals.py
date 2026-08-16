"""
        Created By Hacker Badshah😎
                                                """

"""
     Just Input The Number Whose 
            Roman Numeral You Wants To Know. """
































basic = {1:"I",5:"V",10:"X",50:"L",
         100:"C",500:"D",1000:"M",
         5000:"V\u0305",10000:"C\u0305",
         50000:"L\u0305",100000:"C\u0305",
         500000:"D\u0305",1000000:"M\u0305"}
         
keys = list(basic.keys())
values = list(basic.values())
Roman = ""
i = -1

def bigof(n,gap=0):
    for var in keys:
        if var > n:
            i = keys.index(var)+gap
            return keys[i]

try:
    k = p = input()
    assert float(k).is_integer() and float(k)>0
    k = int(float(k))        
    while k > 0:
        if str(k)[0] == "4":
            Roman += basic[bigof(k,-1)]+basic[bigof(k)]           
            k -= 4*(10**(len(str(k))-1))
        elif str(k)[0] == "9":
            Roman += basic[bigof(k,-2)]+basic[bigof(k)]
            k -= 9*(10**(len(str(k))-1))
        elif k >= keys[i] :
            k -= keys[i]
            Roman += basic[keys[i]] 
        else:
            i -= 1
    print("You Have Enterd :{0}\nAnd In Roman :{1}\n\n".format(p,Roman))
    
except (AssertionError,ValueError):
    print("Please Enter A Natural Number\nAnd not :{0}".format(k)) 
             
except KeyError:
    print("Sorry,But It Can Handle Up to Number 3999999 Only")

finally:
    print("Thanks For Running This Code...")

    
