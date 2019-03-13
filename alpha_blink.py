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
                self.b2 = ["g", "h", "i", "j"]
                self.b3 = ["k", "l", "m", "n"]
                self.b4 = ["o", "p", "q"]
                self.b5 = ["r", "s", "t"]
                self.b6 = ["u", "v", "w"]
                self.b7 = ["x", "y", "z"]
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
                         
               
