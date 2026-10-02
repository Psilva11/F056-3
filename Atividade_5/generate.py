import ROOT 
import numpy as np

f = ROOT.TFile("dados.root","RECREATE")
t = ROOT.TTree("t","gaus_tree")

x = np.array([0.0], dtype=np.float64)
t.Branch("x", x, "x/D")

rd = ROOT.TRandom3(0)

for i in range(10000):
    x[0] = rd.Gaus(0,1)
    t.Fill()

f.cd()
f.Write()
f.Close()
