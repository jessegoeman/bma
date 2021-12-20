import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import simps

#import floats and str seperately
data = np.genfromtxt('data.csv', delimiter=",")
datatext = np.genfromtxt('data.csv', delimiter=",", dtype=None, encoding=None)

timestamps = [int(i.strip("(s)")) for i in datatext[9, 13:]]
A1, A2, A3, A4 = data[10, 13:], data[11, 13:], data[12, 13:], data[13, 13:]
B1, B2, B3, B4 = data[22, 13:], data[23, 13:], data[24, 13:], data[25, 13:]
C1, C2, C3, C4 = data[34, 13:], data[35, 13:], data[36, 13:], data[37, 13:]
D1, D2, D3, D4 = data[46, 13:], data[47, 13:], data[48, 13:], data[49, 13:]
E1, E2, E3, E4 = data[58, 13:], data[59, 13:], data[60, 13:], data[61, 13:]
F1, F2, F3, F4 = data[70, 13:], data[71, 13:], data[72, 13:], data[73, 13:]
G1, G2, G3, G4 = data[82, 13:], data[83, 13:], data[84, 13:], data[85, 13:]
H1, H2, H3, H4 = data[94, 13:], data[95, 13:], data[96, 13:], data[97, 13:]

fig = plt.figure(figsize=(15,8))

plt.subplot(3, 3, 1)
plt.plot(timestamps, A1), plt.plot(timestamps, A2), plt.plot(timestamps, A3), plt.plot(timestamps, A4)
plt.plot(timestamps,H4, "k:"), plt.plot(timestamps,G4,"k--")
plt.legend(["A1 ("+str(simps(A1,x=timestamps).round(2))+")", "A2 ("+str(simps(A2,x=timestamps).round(2))+")"
               ,"A3 ("+str(simps(A3,x=timestamps).round(2))+")", "A4 ("+str(simps(A4,x=timestamps).round(2))+")", "H4 + controle ("+str(simps(H4,x=timestamps).round(2))+")", "G4 - controle ("+str(simps(G4,x=timestamps).round(2))+")"],prop={'size': 8})
plt.xlabel("Tijd (s)"), plt.ylabel("OD 640")
plt.ylim([0.4, 0.9])

plt.subplot(3, 3, 2)
plt.plot(timestamps, B1), plt.plot(timestamps, B2), plt.plot(timestamps, B3), plt.plot(timestamps, B4)
plt.plot(timestamps,H4, "k:"), plt.plot(timestamps,G4,"k--")
plt.legend(["B1 ("+str(simps(B1,x=timestamps).round(2))+")", "B2 ("+str(simps(B2,x=timestamps).round(2))+")"
               ,"B3 ("+str(simps(B3,x=timestamps).round(2))+")", "B4 ("+str(simps(B4,x=timestamps).round(2))+")", "H4 + controle ("+str(simps(H4,x=timestamps).round(2))+")", "G4 - controle ("+str(simps(G4,x=timestamps).round(2))+")"],prop={'size': 8})
plt.xlabel("Tijd (s)"), plt.ylabel("OD 640")
plt.ylim([0.4, 0.9])

plt.subplot(3, 3, 3)
plt.plot(timestamps, C1), plt.plot(timestamps, C2), plt.plot(timestamps, C3), plt.plot(timestamps, C4)
plt.plot(timestamps,H4, "k:"), plt.plot(timestamps,G4,"k--")
plt.legend(["C1 ("+str(simps(C1,x=timestamps).round(2))+")", "C2 ("+str(simps(C2,x=timestamps).round(2))+")"
               ,"C3 ("+str(simps(C3,x=timestamps).round(2))+")", "C4 ("+str(simps(C4,x=timestamps).round(2))+")", "H4 + controle ("+str(simps(H4,x=timestamps).round(2))+")", "G4 - controle ("+str(simps(G4,x=timestamps).round(2))+")"],prop={'size': 8})
plt.xlabel("Tijd (s)"), plt.ylabel("OD 640")
plt.ylim([0.4, 0.9])

plt.subplot(3, 3, 4)
plt.plot(timestamps, D1), plt.plot(timestamps, D2), plt.plot(timestamps, D3), plt.plot(timestamps, D4)
plt.plot(timestamps,H4, "k:"), plt.plot(timestamps,G4,"k--")
plt.legend(["D1 ("+str(simps(D1,x=timestamps).round(2))+")", "D2 ("+str(simps(D2,x=timestamps).round(2))+")"
               ,"D3 ("+str(simps(D3,x=timestamps).round(2))+")", "D4 ("+str(simps(D4,x=timestamps).round(2))+")", "H4 + controle ("+str(simps(H4,x=timestamps).round(2))+")", "G4 - controle ("+str(simps(G4,x=timestamps).round(2))+")"],prop={'size': 8})
plt.xlabel("Tijd (s)"), plt.ylabel("OD 640")
plt.ylim([0.4, 0.9])

plt.subplot(3, 3, 5)
plt.plot(timestamps, E1), plt.plot(timestamps, E2), plt.plot(timestamps, E3), plt.plot(timestamps, E4)
plt.plot(timestamps,H4, "k:"), plt.plot(timestamps,G4,"k--")
plt.legend(["E1 ("+str(simps(E1,x=timestamps).round(2))+")", "E2 ("+str(simps(E2,x=timestamps).round(2))+")"
               ,"E3 ("+str(simps(E3,x=timestamps).round(2))+")", "E4 ("+str(simps(E4,x=timestamps).round(2))+")", "H4 + controle ("+str(simps(H4,x=timestamps).round(2))+")", "G4 - controle ("+str(simps(G4,x=timestamps).round(2))+")"],prop={'size': 8})
plt.xlabel("Tijd (s)"), plt.ylabel("OD 640")
plt.ylim([0.4, 0.9])

plt.subplot(3, 3, 6)
plt.plot(timestamps, F1), plt.plot(timestamps, F2), plt.plot(timestamps, F3), plt.plot(timestamps, F4)
plt.plot(timestamps,H4, "k:"), plt.plot(timestamps,G4,"k--")
plt.legend(["F1 ("+str(simps(F1,x=timestamps).round(2))+")", "F2 ("+str(simps(F2,x=timestamps).round(2))+")"
               ,"F3 ("+str(simps(F3,x=timestamps).round(2))+")", "F4 ("+str(simps(F4,x=timestamps).round(2))+")", "H4 + controle ("+str(simps(H4,x=timestamps).round(2))+")", "G4 - controle ("+str(simps(G4,x=timestamps).round(2))+")"],prop={'size': 8})
plt.xlabel("Tijd (s)"), plt.ylabel("OD 640")
plt.ylim([0.4, 0.9])

plt.subplot(3, 3, 7)
plt.plot(timestamps, G1), plt.plot(timestamps, G2), plt.plot(timestamps, G3)
plt.plot(timestamps,H4, "k:"), plt.plot(timestamps,G4,"k--")
plt.legend(["G1 ("+str(simps(G1,x=timestamps).round(2))+")", "G2 ("+str(simps(G2,x=timestamps).round(2))+")"
               ,"G3 ("+str(simps(G3,x=timestamps).round(2))+")",  "H4 + controle ("+str(simps(H4,x=timestamps).round(2))+")", "G4 - controle ("+str(simps(G4,x=timestamps).round(2))+")"],prop={'size': 8})
plt.xlabel("Tijd (s)"), plt.ylabel("OD 640")
plt.ylim([0.4, 0.9])

plt.subplot(3, 3, 8)
plt.plot(timestamps, H1), plt.plot(timestamps, H2), plt.plot(timestamps, H3),
plt.plot(timestamps,H4, "k:"), plt.plot(timestamps,G4,"k--")
plt.legend(["H1 ("+str(simps(H1,x=timestamps).round(2))+")", "H2 ("+str(simps(H2,x=timestamps).round(2))+")"
               ,"H3 ("+str(simps(H3,x=timestamps).round(2))+")", "H4 + controle ("+str(simps(H4,x=timestamps).round(2))+")", "G4 - controle ("+str(simps(G4,x=timestamps).round(2))+")"],prop={'size': 8})
plt.xlabel("Tijd (s)"), plt.ylabel("OD 640")
plt.ylim([0.4, 0.9])

plt.subplot(3, 3, 9)
plt.text(0,0.5,"in de legendes staan de oppervlaktes onder de curven")
plt.axis('off')

fig.tight_layout()
plt.show()