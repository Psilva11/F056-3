#include "TFile.h"
#include "TTree.h"
#include "TH1F.h"
#include "TCanvas.h"
#include <iostream>
#include "TSystem.h"

int main() {
  if (!gSystem->AccessPathName("dados.root")) {
    std::cout << "Arquivo 'dados.root' encontrado. Prosseguindo com a leitura..." << std::endl;
  } else {
    std::cerr << "Erro: Arquivo 'dados.root' não encontrado. Execute o script 'generate.C' primeiro." << std::endl;
    return 0;
  }
  TFile *f = new TFile("dados.root", "READ");
  TTree *t = (TTree*)f->Get("t");
  TH1F *hist = new TH1F("hist", "Histograma de Valores Gerados", 50, -5, 5);
  TCanvas *c1 = new TCanvas("c1", "Histograma", 800, 600);

  double x;
  t->SetBranchAddress("x", &x);
  Long64_t entries = t->GetEntries();;

  for (Long64_t i = 0; i < entries; i++){
    t->GetEntry(i);
    hist->Fill(x);
  }

  hist->SetLineColor(kBlack);
  hist->SetLineWidth(2);
  hist->SetLineStyle(1);
  hist->SetFillColor(kYellow);
  hist->SetXTitle("Valor gerado");
  hist->GetXaxis()->SetTitleOffset(1.5);
  hist->SetYTitle("Numero de entradas");
  hist->GetYaxis()->SetTitleOffset(1.5);

  c1->SetFillColor(kWhite);

  hist->Fit("gaus");
 
  hist->Draw();
  c1->SaveAs("histograma.png");


  f->Close();

  return 0;
}