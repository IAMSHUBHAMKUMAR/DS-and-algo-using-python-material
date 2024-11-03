class StarCookie:
    milk = 0.1 # global variable
    
    def __init__(self, weight, color) -> None:
        self.weight = weight
        self.color = color

cookie_a = StarCookie(25,"Red")
cookie_b = StarCookie(17,"Blue")
print(cookie_a.__dict__)
print(cookie_b.__dict__)
print(StarCookie.__dict__)
# print(cookie_a.weight)
# print(cookie_a.color)
# print(cookie_a.milk)
# print(cookie_b.weight)
# print(cookie_b.color)
# print(cookie_b.milk)
# print(StarCookie.milk)
# cookie_b = StarCookie()
# cookie_b.weight = 16
# cookie_b.color = "Blue"
# print(cookie_b.weight)
# print(cookie_b.color)
