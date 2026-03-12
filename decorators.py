def greet(fx):
    def mfx():
     print("good morning")
     fx()
     print("thanks for using this function")
    return mfx
@greet
def add():
   print("lets have some fun")

@greet
def sum(a=9,b=7):
   print(a+b)

@greet
def square(u=8):
   return u**u

add()
sum()
square()