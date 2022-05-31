from microbit import *



# show light if
def showLights():
    print('--------------')
    print('show lights')
    print('--------------')
    for x in range(5):
        for y in range(5):
            if matrix[x][y] == 1:
                display.set_pixel(x,y,9)
            else:
                display.set_pixel(x,y,0)
        print()



# Main code -----------------------------------------------

matrix = [ [0]*5 for i in range(5)]



while True:

    readLight = pin0.read_analog() # read analog pin


    # store any left over values into array by adding 1
#    t = readLight / 40 # divide analog pin value by 40 as max value is 1023
    t = readLight - 830 # divide analog pin value by 40 as max value is 1023
    t = t / 4




    for x in range(5):
        for y in range(5):
            if t > 1:
                display.set_pixel(x,y,9)
            else:
                display.set_pixel(x,y,0)
            t = t - 1



#    showLights()
