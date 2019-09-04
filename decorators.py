def kids(func):
    def kids_say():
        print(f'{func()} by the kids')

    return kids_say

def dad(func):
    def dad_says(): 
        print(f'{func()} by dad')

    
    return dad_says

def mom(func):
    def mom_says():
        print(f'{func()} by mom')

    return mom_says
    

@mom
def laundry():
    return "The dirty laundry was cleaned"

laundry()

@kids
def garbage():
    return "The garbage was taken out"

garbage()

@kids
def dust():
    return "The house was dusted"

dust()

@dad
def groom():
    return "The dog was brushed"

groom()

    