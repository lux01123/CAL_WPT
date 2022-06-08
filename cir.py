import math

################# Tham so chung ########################
u =4*3.14*math.pow(10, -7)      # Do tu tham khong khi
r = 3*math.pow(10, -3)          # Ban kinh day dan

################# Tham so cuon day phat ################
Nt = 16                         # So vong day
doutt = 0.29                    # Duong kinh vong ngoai
dint = doutt - (Nt*r*2)         # Duong kinh vong trong
Rt = dint/2                     # Ban kinh vong tron trong
davgt = (doutt + dint)/2 
phit = (doutt + dint)/(doutt - dint)

################ Tham so cuon day thu #################
Nr = 16                         # So vong cuon day thu
doutr = 0.29                    # Duong kinh vong tron ngoai
dinr = doutr - (Nr*r*2)         # Duong kinh vong tron trong
Rr = dinr/2                     # Ban kinh vong tron trong
davgr = (doutr + dinr)/2
phir = (doutr+dinr)/(doutr - dinr)

############### Moi lien he giua hai cuon day #########################
h = 0.08                        # Khoang cach giua hai cuon day
Fk = math.sqrt((4*Rt*Rr)/((Rt*Rt+Rr*Rr)+(h*h)))

############# Cac thong so tinh duoc la ##########################
L1 = ((u*(Nt*Nt)*davgt) / 2)*math.log((2.46/phit) + 0.2*(phit*phit))*math.pow(10, 6)
L2 = ((u*(Nr*Nr)*davgr) / 2)*math.log((2.46/phir) + 0.2*(phir*phir))*math.pow(10, 6)
M = u*Nt*Nr*3.14*math.sqrt(Rt*Rr)*((Fk*Fk*Fk/16) + 3*(Fk*Fk*Fk/64))*math.pow(10, 6)         # Ho cam giua hai cuon day

print("Gia tri cuon phat la L1 :")
print(L1)

print("Gia tri cuon thu la L2 :")
print(L2)

print("Ho cam giua hai cuon day la :")
print(M)
