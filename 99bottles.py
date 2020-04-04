import time as t
bottle = 99
for i in range(99,-1,-1):
    if i>2:
        print(i," bottles of beer in the wall, {} bottles of beer.".format(i))
        print("Take one down and pass it around, {} bottles of beer in the wall.".format(i-1))
    elif i==2:
        print("2 bottles of beer in the wall, 2 bottles of beer.")
        print("Take one down and pass it around, 1 bottle of beer in the wall.")
    elif i==1:
        print("1 bottle of beer in the wall, 1 bottle if beer.")
        print("Take one down and pass it around, no more bottles of beer in the wall.")
    elif i==0:
        print("No more bottles of beer in the wall, no more bottles of beer.")
        print("Go to the store and buy some more, 99 bottles of beer in the wall")
    t.sleep(0.1)
t.sleep(3)    
    
