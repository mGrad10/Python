'''
Melinda Grad
ASM 9
singleton.py
'''

class Singleton:
    # {cls -->instance}
    _singleton = {}

    # Takes in a class
    def __new__(cls):
        if cls not in Singleton._singleton:
            # This creates the instance for this class
            Singleton._singleton[cls] = object.__new__(cls)

        return Singleton._singleton[cls]


if __name__ == '__main__':

    class C(Singleton):
        pass

c1 = C()
c2 = C()

print(id(c1), id(c2))
