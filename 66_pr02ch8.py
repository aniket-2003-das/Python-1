# To convert celcius to farenheit.

def farh(cel):
    return ( cel * (9/5) ) + 32

c = 100
f = farh(c)

print("farenheit temp is:" + str(f))
