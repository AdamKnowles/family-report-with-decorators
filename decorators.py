def kids(func):
    def kids_say():
        func()
        print("by the kids")

    return kids_say

def dad(func):
    def dad_says():
        func()
        print("by dad")

    
    return dad_says

def mom(func):
    def mom_says():
        func()
        print("by mom")

    return mom_says
    

@mom
def laundry():
    print("The dirty laundry was cleaned")

laundry()

@kids
def garbage():
    print ("The garbage was taken out")

garbage()

@kids
def dust():
    print ("The house was dusted")

dust()

@dad
def groom():
    print ("The dog was brushed")

groom()

    