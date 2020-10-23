
# BEST WEIGHTS SO FAR 10/22/2020
_pW = 2 
_kW = 4.563486995637862 
_minDW = -0.20805803766397996 
_capSW = 1.363555349866284 
_eCW = -0.18493943623434173

x = [_pW,_kW,_minDW,_capSW,_eCW]
file2write=open("values",'w')
file2write.write("here goes the data\n")
file2write.write("_pW = "+str(_pW)+"\n_kW = "+str(_kW)+"\n_minDW = "+str(_minDW)+"\n_capSW = "+str(_capSW)+"\n_eCW = "+str(_eCW)+"\n")
file2write.close()
