#include "Pythia8/Pythia.h"
using namespace Pythia8;

int main(){
  Pythia pythia;
  
  pythia.readString("Beams:eCM = 13000");
  pythia.readString("Top:qqbar2ttbar = on");
  pythia.readString("Top:gg2ttbar = on");

  pythia.init();

  int Nevt = 10000;

  for (int ievt = 0; ievt < Nevt; ++ievt){
    if (!pythia.next()) continue;
  }

  pythia.stat();

  double SigmaGen = pythia.info.sigmaGen()*1e9;
  double SigmaErr = pythia.info.sigmaErr()*1e9;
  
  std::cout << "Sigma :\t" << SigmaGen << " +- "
            << SigmaErr << " pb" << std::endl;
  return 0;
}
