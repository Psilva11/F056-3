#include "SimTrack.h"
#include <iostream>

int main() {
  
  SimTrack t1(10.0, 3.0, 4.0, 5.0, 11, 23); // Elétron
  SimTrack t2(15.0, 0.0, 0.0, 10.0, 211, 22); // Píon+

  std::cout << "--- Particula 1 ---" << std::endl;
  std::cout << "pT:\t" << t1.Pt() << std::endl;
  std::cout << "Eta:\t" << t1.Eta() << std::endl;
  std::cout << "ID da Partícula:\t" << t1.ParticleId() << std::endl;
  std::cout << "ID Partícula-mãe:\t" << t1.ParentId() << "\n" << std::endl;

  std::cout << "--- Particula 2  ---" << std::endl;
  std::cout << "pT: \t" << t2.Pt() << std::endl;
  std::cout << "Eta: \t" << t2.Eta() <<  std::endl;
  std::cout << "ID da Partícula:\t" << t2.ParticleId() << std::endl;
  std::cout << "ID Partícula-mãe:\t" << t2.ParentId() << std::endl;

  return 0;
}