#include <stdio.h>
#include <iostream>
#include <cstdlib>

int main(int argc, char *argv[]){
  if((argc-1)!=1){
    std::cout << "Número de parâmetros incorreto. Abortando programa." << std::endl;
    return 0;
  }

  int num = std::atoi(argv[1]);

  std::cout << "Hello world " << num << std::endl;
  return 0;
}