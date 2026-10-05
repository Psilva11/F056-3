# Atividade 7

## Tabela Comparativa

| Gerador | $\sigma$ (pb) | Incerteza (pb) | PDF |
| :--- | :--- | :--- | :--- |
| **Pythia8** | 507.7 | 2.594 | NNPDF2.3 QCD+QED LO |
| **MadGraph5_aMC@NLO** | 505.8 | 0.73 | nn23lo1 (NNPDF2.3 LO) |

---

## Respostas da Discussão

**1. Concordância dos valores:**
Os valores encontrados para a seção de choque de ambos geradores batem dentro das incertezas apresentadas, como visto na tabela acima.

**2. Ordem perturbativa e PDFs:**
Ambos os cálculos foram realizados na mesma ordem em teoria de perturbação e utilizando a mesma família de PDFs como podemos conferir através de `log_pythia` e `crossx.html`. Por estarem na mesma ordem perturbativa, garantimos que os cálculos da seção de choque e que a parametrização das distribuições não tenham resultados muito discrepantes.

**3. Inclusão do canal gg no Pythia8:**
A flag `Top:qqbar2ttbar` inclui apenas a aniquilação quark-antiquark. Então, **decidi ativar também o canal de fusão de glúons** (`Top:gg2ttbar = on`). Em colisões com energia à nível LHC (13 TeV) a produção por fusão de glúons é o mecanismo dominante de produção (~90% da seção de choque total, segundo: *[PDG](https://pdg.lbl.gov/2026/reviews/rpp2026-rev-top-quark.pdf))*. Logo, deixa-lo de fora geraria uma grande diferença entre as seções de choque, dado que o comando `generate p p > t t~` do MadGraph já considera ambos mecanismos (soma automaticamente todos os subprocessos partônicos). 

**4. Outras fontes de diferença:**
Além da estatística de eventos gerados, algumas possíveis causas de diferenças podem ser:
* **Escolha das escalas de fatoração ($\mu_F$) e renormalização ($\mu_R$):** Apesar dos dois geradores usarem escalas dinâmicas, eles podem adotar definições matemáticas diferentes para definir essa escala, o que pode levar a pequenas variações na seção de choque.


**5. Impacto do Parton Shower no MadGraph:**
Se incluíssemos o cálculo de parton shower do MadGraph via Pythia8, a **seção de choque total reportada não mudaria**. A probabilidade total do processo hard é determinada em nível partônico e calculada pelo elemento de matriz. O parton shower apenas adiciona as radiações *ISR/FSR* e gera jatos.