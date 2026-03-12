class myclass:
    def __int__(self,value):
        self._value=value
    def king(self):
        print(f"value is {self._value}")
    def queen(self):
        return 10* self._value
    
obj= myclass()
# obj.show() 
obj.queen()