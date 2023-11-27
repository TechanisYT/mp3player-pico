# mp3player.py
# Johannes Melcher-Millner 4AHEL
# HTL-Rankweil 2023/24
# 23.10.2023

from dfplayermini import Player
from machine import Pin
from time import sleep, sleep_ms

from picographics import PicoGraphics, DISPLAY_PICO_EXPLORER, PEN_P8

display = PicoGraphics(display=DISPLAY_PICO_EXPLORER, pen_type=PEN_P8)
display.set_font("bitmap8")

BLACK = display.create_pen(0, 0, 0)
RED = display.create_pen(255, 0, 0)
WHITE = display.create_pen(255, 255, 255)
GRAY = display.create_pen(150,150,150)
GREEN = display.create_pen(0,255,0)


music = Player(pin_TX=Pin(4), pin_RX=Pin(5))
pp = Pin(12, Pin.IN, Pin.PULL_UP)
skip = Pin(13, Pin.IN, Pin.PULL_UP)
v_up = Pin(14, Pin.IN, Pin.PULL_UP)
v_down = Pin(15, Pin.IN, Pin.PULL_UP)

pp_prev = True
skip_prev = True
v_up_prev = True
v_down_prev = True
playing = True
volume = 15
track = 0

tracks = ["Dont Look Back in Anger(Oasis)", "Have You Ever Seen The Rrain(clearwater)", "Hold the Line(TOTO)", "Jeanny(Falco)", "Just Cant get Enough(Depeche Mode)", "Kein Problem(Apache 207)", "Schmusen statt Snusn(Wildkogel Buam)", "Feuer Wasser Sturm(Niclov)"]

music.module_reset()
music.play(track)
#music.set_volume(volume)
print("playing: " + str(playing))

while True:
    if not pp.value() and pp.value() != pp_prev:
        print("play/pause")
        playing = ~playing
        if playing == True:
            music.pause()
            print("pause")
        else:
            music.play()
            print("track: " + tracks[track])
            print("play")
        while not pp.value():
            pp_prev = False
        pp_prev = True
    if not skip.value() and skip.value() != skip_prev:
        print("skip")
        track = track + 1
        music.play("next")
        print("playing track: " + str(track))
        while not skip.value():
            skip_prev = False
        skip_prev = True
    if not v_up.value():
        if volume < 40:
            print("volume up")
            music.volume_up()
            volume = volume + 1
            print("volume " + str(volume))
        else:
            print("max volume")
        sleep_ms(200)
    if not v_down.value():
        if volume > 0:
            print("volume down")
            music.volume_down()
            volume = volume - 1
            print("volume " + str(volume))
        else:
            print("min volume")
        sleep_ms(200)
    display.set_pen(BLACK)
    display.clear()
    display.set_pen(WHITE)
    display.text("track: ", 0, 20, scale=3)
    display.text(tracks[track], 0, 50, scale=2)
    display.text("next track: ", 0, 80, scale=3)
    display.text(tracks[track + 1], 0, 110, scale=2)
    display.text("volume: " + str(volume), 0, 140, scale=3)
    if playing == True:
        display.text("playing", 0, 170, scale=3)
    else:
        display.text("paused", 0, 170, scale=3)
    display.update()