import math
from re import A

n = 1123

while (n > 0):

	print("Tham so cuon day phat")
	Nt = float(input("Nhap gia tri so vong day phat: "))
	doutt = float(input("Nhap duong kinh vong tron ngoai: "))

	print()	# xuong dong

	print("Tham so cuon day thu")
	Nr = float(input("Nhap gia tri so vong day thu: "))
	doutr = float(input("Nhap duong kinh vong tron ngoai: "))

	print()	# xuong dong

#	h = float(input("Nhap khoang cach giua 2 cuon day: "))
	h = 0.08
	print() 

	f = float(input("Nhap gia tri tan so cong huong: "))


################# Tham so chung ########################
	u = 4*3.14*math.pow(10, -7)      # Do tu tham khong khi
	r = 0.7*math.pow(10, -3)          # Ban kinh day dan

################# Tham so cuon day phat ################
#/Nt = 16                         # So vong day
#doutt = 0.29                    # Duong kinh vong ngoai
	dint = doutt - (Nt*r*2*2)         # Duong kinh vong trong
	Rt = doutt/2                     # Ban kinh vong tron ngoai
	davgt = (doutt + dint)/2 
	phit = (doutt - dint)/(doutt + dint)

################ Tham so cuon day thu #################
#Nr = 16                         # So vong cuon day thu
#doutr = 0.29                    # Duong kinh vong tron ngoai
	dinr = doutr - (Nr*r*2*2)         # Duong kinh vong tron trong
	Rr = doutr/2                     # Ban kinh vong tron ngoai
	davgr = (doutr + dinr)/2
	phir = (doutr - dinr)/(doutr + dinr)

############### Moi lien he giua hai cuon day #########################
	Fk = math.sqrt((4*Rt*Rr)/((Rt*Rt+Rr*Rr)+(h*h)))

############# Cac thong so tinh duoc la ##########################
	L1 = ((u*(Nt*Nt)*davgt) / 2)*math.log((2.46/phit) + 0.2*(phit*phit))*math.pow(10, 6)
	L2 = ((u*(Nr*Nr)*davgr) / 2)*math.log((2.46/phir) + 0.2*(phir*phir))*math.pow(10, 6)
	M = u*Nt*Nr*3.14*math.sqrt(Rt*Rr)*((Fk*Fk*Fk/16) + 3*(Fk*Fk*Fk/64))*math.pow(10, 6)         # Ho cam giua hai cuon day

############### Tinh gia tri tro khang cuon day ##################
	p = 1.68*math.pow(10, -8)
	
	lt = 3.14*((doutt + dint)/2)*Nt
	lr = 3.14*((doutr + dinr)/2)*Nr

	a = 3.14*r*r

	r1 = ((p*lt)/a)*math.pow(10, 3)
	r2 = ((p*lr)/a)*math.pow(10, 3)
####### Tinh gia tri he so pham chat cuon day ####################
	q1 = ((2*3.14*f*L1)/r1)*math.pow(10, -3)
	q2 = ((2*3.14*f*L2)/r2)*math.pow(10, -3)
####### He so ghep noi ##########################
	k = (M*math.pow(10, -6))/(math.sqrt((L1*math.pow(10, -6))*(L2*math.pow(10, -6))))
###### Tinh tro khang tai toi da #############
	rlm = 1 + math.sqrt(((2*3.14*f)*(2*3.14*f)*M*M*math.pow(10, -6))/(r1*r2))

	if dint < 0:
		print("Gia tri nhap vao sai")

	else :
		print("Gia tri cuon phat la L1 uH :")
		print("%.3f " % round(L1, 3))

		print("Gia tri cuon thu la L2 uH :")
		print("{0:.3f} ".format(L2))

		print("Ho cam giua hai cuon day la M uH :")
		print("%.3f " % round(M,3))

		print("Dien tro cuon phat la R1 m Ôm : ")
		print("%.3f " % round(r1,3))

		print("Dien tro cuon thu la R2 m Ôm : ")
		print("%.3f " % round(r2,3))

		print("He so pham chat cuon day phat q1: ")
		print("%.3f" % round(q1, 3))

		print("He so pham chat cuon day thu q2: ")
		print("%.3f" % round(q2, 3))

		print("He so ho cam k: ")
		print("%.3f" % round(k, 3))

		print("Tro khang tai toi da:")
		print("%.3f" % round(rlm, 3))
		
		print("end")

		n = n - 1
		print()
