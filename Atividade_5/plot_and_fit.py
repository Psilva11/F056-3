import ROOT
import numpy as np

if not ROOT.gSystem.AccessPathName("dados.root"):
    print("Arquivo 'dados.root' encontrado. Prosseguindo com a leitura...")
else:
    print("Erro: Arquivo 'dados.root' não encontrado. Execute o script 'generate.C' primeiro.")
    exit()

f = ROOT.TFile("dados.root", "READ")
t = f.Get("t")
hist = ROOT.TH1F("hist", "Histograma de Valores Gerados", 50, -5, 5)
c1 = ROOT.TCanvas("c1", "Histograma", 800, 600)

for i in t:
    hist.Fill(i.x)

hist.SetLineColor(ROOT.kBlack)
hist.SetLineWidth(2)
hist.SetLineStyle(1)
hist.SetFillColor(ROOT.kYellow)
hist.GetXaxis().SetTitle("Valor Gerado")
hist.GetYaxis().SetTitleOffset(1.5)
hist.GetYaxis().SetTitle("Numero de entradas")
hist.GetYaxis().SetTitleOffset(1.5)

c1.SetFillColor(ROOT.kWhite)

hist.Fit("gaus")

hist.Draw()
c1.SaveAs("histograma.png")

f.Close()