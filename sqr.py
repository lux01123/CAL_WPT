import math

#Tham so chung
u = 4*3.14*math.pow(10, -7)      # Do tu tham khong khi
r = 0.91*math.pow(10, -3)      # Ban kinh day dan
s = 1*math.pow(10, -3)        # Khe ho giua cac vong day

# Tham so cuon day phat
Nt = 22     #So vong day
doutt = 0.33        # Chieu dai vong ngoai
dint = doutt - 2*(Nt*2*r+(Nt-1)*s)     # Chieu dai vong trong
davgt = (doutt + dint)/2 
phit = (doutt + dint)/(doutt - dint)

#Tham so cuon day thu
Nr = 22     # So vong cuon day thu
doutr = 0.33        # Chieu dai vong ngoai
dinr = doutr - 2*(Nr*2*r+(Nr-1)*s)     # Chieu dai vong trong
davgr = (doutr + dinr)/2
phir = (doutr+dinr)/(doutr - dinr)

#Moi lien he giua hai cuon day
h = 0.1     # Khoang cach giua hai cuon day
b = math.sqrt(davgt*davgt + h*h)
x = math.sqrt(2*davgt*davgt + h*h)

# Cac thong so tinh duoc la
L1 = 2.34*u*((Nt*Nt*davgt)/(1+2.75*phit))*math.pow(10, 6)
L2 = 2.34*u*((Nr*Nr*davgr)/(1+2.75*phir))*math.pow(10, 6)
M =(2*Nt*u/3.14)*(math.log(((davgt+b)/(davgt+x))*(b/h)) + (x-2*b+h))*math.pow(10, 6)        # Ho cam giua hai cuon day

print("Gia tri cuon phat la L1 = "  )
print(L1)

print("Gia tri cuon thu la L2 = ")
print(L2)

print("Ho cam giua hai cuon day la")
print(M)