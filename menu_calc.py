ch = 'y'
while(ch=='y'):
    print("""RATE LIST:
          1)Chicken Strips - $3.50
          2)French Fries - $2.50
          3)Hamburger - $4.00
          4)Hotdog - $3.50
          5)Large Drink - $1.75
          6)Medium Drink - $1.50
          7)Milk Shake - $2.25
          8)Salad - $3.75
          9)Small Drink - $1.25""")
    print("Place your order:")
    n = int(input())
    bill=0.0
    x=0
    i=0
    rates={1:3.5,2:2.5,3:4.0,4:3.50,5:1.75,6:1.5,7:2.25,8:3.75,9:1.25}
    while(n>0):        
        x=n%10
        bill=bill+rates.get(x)
        n=n//10
        i+=1
    print("Total items ordered are:",i)
    print("The above order costs:$",bill)
    print("Want to make more orders ? y/n")
    ch=input()


    
