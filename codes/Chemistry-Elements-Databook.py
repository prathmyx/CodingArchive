"""
          Created by Hacker Badshah😎
                                             """
                                              
"""
    Input the Atomic Number or Name or Symbol
                and get other information with
                        Electron Configuration.   
                                             """


"""
    Or Input any word to see if can be broken 
                down to Elements Name    
                                             """








"""
   These  Electron Configuration are maded
          so they aren't correct with the 
               exception  elements.
                                             """













Elements = {"H":"Hydrogen","He":"Helium","Li":"Lithium","Be":"Beryllium","B":"Boron","C":"Carbon","N":"Nitrogen","O":"Oxygen","F":"Fluorine","Ne":"Neon","Na":"Sodium","Mg":"Magnesium","Al":"Aluminium","Si":"Silicon","P":"Phosphorus","S":"Sulfur","Cl":"Chlorine","Ar":"Argon","K":"Potassium","Ca":"Calcium","Sc":"Scandium","Ti":"Titanium","V":"Vanadium","Cr":"Chromium","Mn":"Manganese","Fe":"Iron","Co":"Cobalt","Ni":"Nickel","Cu":"Copper","Zn":"Zinc","Ga":"Gallium","Ge":"Germanium","As":"Arsenic","Se":"Selenium","Br":"Bromine","Kr":"Krypton","Rb":"Rubidium","Sr":"Strontium","Y":"Yttrium","Zr":"Zirconium","Nb":"Niobium","Mo":"Molybdenum","Tc":"Technetium","Ru":"Ruthenium","Rh":"Rhodium","Pd":"Palladium","Ag":"Silver","Cd":"Cadmium","In":"Indium","Sn":"Tin","Sb":"Antimony","Te":"Tellurium","I":"Iodine","Xe":"Xenon","Cs":"Cesium","Ba":"Barium","La":"Lanthanum","Ce":"Cerium","Pr":"Praseodymium","Nd":"Neodymium","Pm":"Promethium","Sm":"Samarium","Eu":"Europium","Gd":"Gadolinium","Tb":"Terbium","Dy":"Dysprosium","Ho":"Holmium","Er":"Erbium","Tm":"Thulium","Yb":"Ytterbium","Lu":"Lutetium","Hf":"Hafnium","Ta":"Tantalum","W":"Tungsten","Re":"Rhenium","Os":"Osmium","Ir":"Iridium","Pt":"Platinum","Au":"Gold","Hg":"Mercury","Tl":"Thallium","Pb":"Lead","Bi":"Bismuth","Po":"Polonium","At":"Astatine","Rn":"Radon","Fr":"Francium","Ra":"Radium","Ac":"Actinium","Th":"Thorium","Pa":"Protactinium","U":"Uranium","Np":"Neptunium","Pu":"Plutonium","Am":"Americium","Cm":"Curium","Bk":"Berkelium","Cf":"Californium","Es":"Einsteinium","Fm":"Fermium","Md":"Mendelevium","No":"Nobelium","Lr":"Lawrencium","Rf":"Rutherfordium","Db":"Dubnium","Sg":"Seaborgium","Bh":"Bohrium","Hs":"Hassium","Mt":"Meitnerium","Ds":"Darmstadtium","Rg":"Roentgenium","Cn":"Copernicium","Nh":"Nihonium","Fl":"Flerovium","Mc":"Moscovium","Lv":"Livermorium","Ts":"Tennessine","Og":"Oganesson"}

keys = list(Elements.keys())
values = list(Elements.values())

#Code for Electron Configuration
def Econfi(a):
    Sup = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    order = [" 1s2"," 2s2"," 2p6"," 3s2"," 3p6",
" 4s2"," 3d10"," 4p6"," 5s2"," 4d10"," 5p6",
" 6s2"," 4f14"," 5d10"," 6p6"," 7s2"," 5f14",
" 6d10"," 7p6"]
    Econfi = ""
    i = 0
    
    if a > 86:
        Econfi,i,a = "[Rn]",15,a-86
    elif a > 54:
        Econfi,i,a = "[Xe]",11,a-54
    elif a > 36:
        Econfi,i,a = "[Kr]",8,a-36
    elif a > 18:
        Econfi,i,a = "[Ar]",5,a-18
    elif a > 10:
        Econfi,i,a = "[Ne]",3,a-10
    elif a > 2:
        Econfi,i,a = "[He]",1,a-2
    
    while a > 0:
        a -= int(order[i][3:])
        if a < 0:
            Econfi += order[i][:3] + str(int(order[i][3:]) + a).translate(Sup)
        elif a >= 0:
            Econfi += order[i][:3]+order[i][3:].translate(Sup) 
        i += 1
    
    return Econfi

#Finding all permutation posssible for string
def groups(n):
    if n == 0:
        return [[]]
    elif n == 1:
        return [[1]]
    else :
        return [i + [1] for i in groups(n-1)] + [i + [2] for i in groups(n-2)]

#Getting arrays of Index to cut
def cutter(x):
    perms = groups(len(x))
    for arr in perms:
        #changing into index
        arr = [sum(arr[:i]) for i in range(len(arr))] 
        #cutting string
        data = [x[i:j] for i,j in zip(arr,arr[1:]+[None])]
        yield data

#iterating through all possibility and finding answer
def checker(str):
    data = []
    for words in cutter(str):
        words = list(map(lambda x:x.title(),words))
        if all(list(map(lambda x:x in keys,words))):
            for i in words:
                word = "["+i+"]"+Elements[i]
                data.append(word)
        else:
            continue
        data.append(" ")
    return data


a = input().strip()
try:
    if a.isalpha():
        b = a.title()
        ans = checker(b)

        if b in keys:
                                                                               print("Your Input:"+a,"\n\nSymbol :'"+b+"'\nName :",Elements[b],"\nAtomic Number :",keys.index(b)+1,"\nElectron Configuration :",Econfi(keys.index(b)+1))
            
        elif ans != []:
            print(b,"can be written as")
            print("\n".join(ans))
            
        elif b in values:
            print("Your Input:"+a,"\n\nSymbol :'"+keys[values.index(b)]+"'\nName :",b,"\nAtomic Number :",values.index(b)+1,"\nElectron Configuration :",Econfi(values.index(b)+1)) 
        
        else:
            print(a,",It doesn't match with any Element or can be broken down to Elements")
    
    elif a.isdigit() or  int(a) < 0:
        a = int(a)
        if a < 0:
            print("Please enter a positive number.We dont have negative atomic number in this world")
        elif a == 0:
            print("I think you love zero a lot but please enter a valid Atomic Number")
        elif a > 118:
            print("Sorry,but in this planet we only have discovered 118 elements till now.\nAnd you entered:",a)
        else:
            print("Your Input:"+str(a),"\n\nSymbol :'"+keys[a-1]+"'\nName :",values[a-1],"\nAtomic Number :",a,"\nElectron Configuration :",Econfi(a))

except ValueError:
    print("Please enter something in Human format.\nYou have entered:",a)

finally:
    print("\nThanks For Visiting.I hope you like it.")

