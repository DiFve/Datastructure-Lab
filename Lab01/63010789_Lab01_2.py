h,w = input("Enter your High and Weight : ").split()
h = float(h)
w = float(w)
bmi=w/(h*h)
if(bmi<18.50):
    print("Less Weight")
elif(18.50 <= bmi <23):
    print("Normal Weight")
elif(23<=bmi<25):
    print("More than Normal Weight")
elif(25<=bmi<30):
    print("Getting Fat")
else:
    print("Fat")