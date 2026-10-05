#!/bin/bash

# Verificando se o executável existe
if [ ! -x "./main" ]; then
  echo " --- ERRO: Executável './main' não foi encontrado ----"
  exit 1
fi

echo "Simulando em paralelo..."

./main main_higgs.cmnd higgs.root &
./main QCD_bckg.cmnd qcd_bckg.root &
./main ZJET_bckg.cmnd zjet_bckg.root &
./main TTBAR_bckg.cmnd ttbar_bckg.root &

wait 

# Troubleshooting
echo "---- Verificando arquivos ----" 
ERRO=0

for config in *.cmnd; do
  nome_base="${config%.cmnd}"
  nome_base="${nome_base,,}"
  nome_base="${nome_base#main_}"

  arquivo="${nome_base}.root"
  
  if [ ! -f "$arquivo" ]; then
    echo "FALHA: Arquivo $arquivo nao foi gerado!"
    ERRO=1
  fi
done

echo "Finalizado e todos arquivos .root foram gerados!"