#include "SimpleMET.h"
#include <iostream>

int main() {
  SimpleMET meu_MET;

  double px1 = 10.0, py1 = 5.0;
  double px2 = -3.0, py2 = 4.0;
  double px3 = -10.0, py3 = -5.0;
  
  if ((px1 + px2) || (py1 + py3)){
    std::cout << "Erro: Resultado não-físico detectado.\nSoma de vetores opostos deve ser 0." << std::endl;
    return 0;
  }

  meu_MET.Add(px1, py1);
  meu_MET.Add(px2, py2);
  meu_MET.Add(px3, py3);

  std::cout << "MET Resultante:\t " << meu_MET.Value() << "\nPhi Resultante:\t" << meu_MET.Phi() << std::endl;
  return 0;
}