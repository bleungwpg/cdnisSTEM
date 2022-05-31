from microbit import *



# Main code -----------------------------------------------
# -------------- explanation of how the code works
# the goal is to get the variable t to have a value of about 25 during regular room light
# this way all the lights should be on in the following double loop
# when resistance to the LDR increases the value should drop to 0


# create a 2D array
matrix = [ [0]*5 for i in range(5)]



while True:

    readLight = pin0.read_analog() # read analog pin from pin 0



# ---------------------------------- STUDENT'S SHOULD ONLY MODIFY CODE HERE ----------------------------------
    t = readLight - 790 # divide analog pin value by 40 as max value is 1023
    t = t / 4
# ---------------------------------- STUDENT'S SHOULD ONLY MODIFY CODE HERE ----------------------------------


    # go through matrix and show light for the value of t
    for x in range(5):
        for y in range(5):
            if t > 1:
                display.set_pixel(x,y,9)
            else:
                display.set_pixel(x,y,0)
            t = t - 1

