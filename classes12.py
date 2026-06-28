class India():
    def capital(self):
        print("New Delhi")
    def language(self):
        print("Hindi")
    def type(self):
        print("developing.")
class USA():
    def capital(self):
        print("Washington, D.C.")
    def language(self):
        print("English")
    def type(self):
        print("developed country.")
i = India()
u = USA()
for x in (i,u):
    x.capital()
    x.language()
    x.type()
