import ROOT

c1 = ROOT.TCanvas("c1", "mH_GeV", 800, 600)

arquivos = {
  "Sinal": ("higgs.root", ROOT.kRed),
  "Background QCD": ("qcd_bckg.root", ROOT.kBlue),
  "Background ZJET": ("zjet_bckg.root", ROOT.kGreen),
  "Background TTBAR": ("ttbar_bckg.root", ROOT.kMagenta)
}

leg = ROOT.TLegend(0.65,0.65,0.88,0.85)
leg.SetBorderSize(0)

hists = []

for key, (nome, cor) in arquivos.items():
  arquivo = ROOT.TFile(nome)

  tree = arquivo.Get("t")

  if not tree:
    print(f"---- ERRO: Tree nao encontrada em {nome}")
    continue

  hist_nome = f"hist_{nome}"
  hist = ROOT.TH1F(hist_nome, "Distribuicao de Massa Invariante (b#bar{b}); Massa m_{b#bar{b}} (GeV); Eventos", 60, 0, 200)

  tree.Draw(f"mH >> {hist_nome}", "", "goff")

  hist.SetLineColor(cor)
  hist.SetLineWidth(2)
  hist.SetStats(0)
  hist.SetDirectory(0)

  if key == "Sinal":
    hist.SetMaximum(hist.GetMaximum()*1.5)
    hist.Draw("H")
  else:
    hist.Draw("SAME")

  leg.AddEntry(hist, key, "l")
  hists.append(hist)

  arquivo.Close()

leg.Draw()
c1.Update()

c1.SaveAs("Histograma_mH.png")

print("---- Grafico plotado com sucesso. ----")