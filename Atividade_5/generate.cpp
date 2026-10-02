#include "TFile.h"
#include "TTree.h"
#include "TRandom3.h"

int main(){

  TFile *f = new TFile("dados.root", "RECREATE");
  TTree *t = new TTree("t", "gaus_tree");
    
  double x;
  t->Branch("x", &x, "x/D");

  TRandom3 rnd(0);
  for (int i = 0; i < 1000; i++) {
    x = rnd.Gaus(0, 1);
    t->Fill();
  }

  f->cd();
  t->Write();
  f->Close();

  return 0;
}