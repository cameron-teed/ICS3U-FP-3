#!usr/bin/env python

# Created by: Cameron Teed
# Created On: October 2019
# This program puts sprites on the screen 

import ugame
import stage

# an image bank for CircuitPython
bank = stage.Bank.from_bmp16("space_aliens.bmp")

sprites = []


def main():


    # sets the backround to the image 0 in the bank
    # if your 0 image is magenta, your backround will most lickley be distorted
    # backrounds do not have megenta as a transparent color
    background = stage.Grid(bank, 10, 8)

    alien = stage.Sprite(bank, 9, 64, 56)
    sprites.append(alien)
    ship = stage.Sprite(bank, 5, 75, 56)
    sprites.insert(0, ship)

    # create a stage for the backround to show up on
    #     and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, 60)
    # set the backround layer
    game.layers = sprites + [background]
    # render the backround
    # most likely you will only render backound once per scene
    game.render_block()

    while True:

        game.render_sprites(sprites)
        game.tick()


if __name__ == "__main__":
    main()
