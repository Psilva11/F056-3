#include "Pythia8/Pythia.h"
#include "TFile.h"
#include "TTree.h"
#include <iostream> 

using namespace Pythia8;

int main(int argc, char* argv[]){
  if (argc != 3){
    std::cerr << "Para rodar isoladamente, use: ./main <mode_config.cmnd> <mode.root>" << std::endl;
    return 1;
  }

  Pythia pythia;
  pythia.readFile(argv[1]);
  pythia.init();

  TFile *f = new TFile(argv[2], "RECREATE");
  TTree *t = new TTree("t", "HiggsMass_Tree");
  
  double mH;
  t->Branch("mH", &mH, "mH/D");

  int nEvt = pythia.mode("Main:numberOfEvents");

  for (int evt = 0; evt < nEvt; ++evt){
    if (!pythia.next()){continue;}
    Vec4 pH(0.,0.,0.,0.);
    int nBQuarks = 0;

    for (int i = 0; i < pythia.event.size(); ++i) {
      if (abs(pythia.event[i].id()) == 5) {
        
        int idxMother = pythia.event[i].mother1();
        if (idxMother > 0) {
          int idMother = abs(pythia.event[idxMother].id());
          bool maeValida = (idMother == 25 || idMother == 23 || idMother == 6 || idMother == 21 || (idMother >= 1 && idMother <= 5));

          if (maeValida) {
            pH += pythia.event[i].p();
            nBQuarks++;
          }
        }
      }

      if (nBQuarks == 2) {
        mH = pH.mCalc();
        t->Fill();
        break; 
      }
    }
  }

  pythia.stat();
  f->cd();
  t->Write();
  f->Close();

  return 0;
}