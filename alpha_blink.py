import blinkt
blinkt.set_clear_on_exit()
import time
class AlphaBlink():
        def __init__(self):
                blinkt.set_all(0,255,0)
                blinkt.show()
                time.sleep(2)
                blinkt.clear()
                blinkt.show()
                self.b0 = ["a", "b", "c"]
                self.b1 = ["d", "e", "f"]
        def print_blinkt(self, ltt):
                letter=ltt.lower()
                if letter in self.b0:
                        print("a,b,c")
                        rn = (self.b0.index(letter) + 1)
                        for i in range(rn):
                            blinkt.set_pixel(0,255,0,0)
                            blinkt.show()
                            time.sleep(0.5)
                            blinkt.clear()
                            blinkt.show()
                            time.sleep(0.5)
                if letter in self.b1:
                        print("d,e,f")
                        rn = (self.b1.index(letter) + 1)
                        for i in range(rn):
                            blinkt.set_pixel(1,255,0,0)
                            blinkt.show()
                            time.sleep(0.5)
                            blinkt.clear()
                            blinkt.show()
                            time.sleep(0.5)



