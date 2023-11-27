from dfplayermini import Player
from machine import Pin

from time import sleep, sleep_ms

music = Player(pin_TX=Pin(4), pin_RX=Pin(5))
pp = Pin(12, Pin.IN, Pin.PULL_UP)
skip = Pin(13, Pin.IN, Pin.PULL_UP)
v_up = Pin(14, Pin.IN, Pin.PULL_UP)
v_down = Pin(15, Pin.IN, Pin.PULL_UP)

#print("set volume")
#music.volume(20)

#print("start play")
#music.play(1)
#sleep(2)

#print("stop play with fadeout")
#music.fadeout(2000)

#music.play('next')
#sleep(10)

#music.pause()
#sleep(3)

#music.loop()
#music.play(2)
#sleep(20)
pp_prev = True
skip_prev = True
v_up_prev = True
v_down_prev = True
playing = False
volume = 20

music.play(1)
print(playing)

while True:
    if not pp.value() and pp.value() != pp_prev:
        print("play/pause")
        playing = ~playing
        if playing:
            music.pause()
        else:
            music.resume()
        while not pp.value():
            pp_prev = False
        pp_prev = True
    if not skip.value() and skip.value() != skip_prev:
        print("skip")
        while not skip.value():
            skip_prev = False
        skip_prev = True
    if not v_up.value():
        print("volume up")
        volume = volume + 1
        music.volume(volume)
        sleep_ms(150)
    if not v_down.value():
        print("volume down")
        volume = volume - 1
        music.volume(volume)
        sleep_ms(150)