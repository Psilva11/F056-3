# Atividade 6

# Justificativas do .cmnd 
Inicialmente ao tentar rodar o Pythia com LHAPDF6, houve um erro e não foi possível carregar a PDF: `PYTHIA Error in dlopen_plugin: libpythia8lhapdf6.so: cannot open shared object file: No such file or directory`. Então, a flag `LHAPDF6:cteq6l1` foi desabilitada no *.cmnd*, usando a opção default que possui precisão semelhante na simulação, logo o impacto dessa escolha não é relevante para este caso.

Além disso, foram ligadas apenas as configurações padrões e sugestões, afim de estudar apenas o canal dominante com a simulação mais básica e genérica possível.

---

# Execução
Para compilar, rodar a simulação e gerar os gráficos, execute no terminal:

```bash
make main
chmod +x run_all.sh
./run_all.sh
python3 plotting.py
