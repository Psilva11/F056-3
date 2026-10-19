# Atividade 8  

---

## Problema 1: Histograma dos Dados e PDF Teórica
**Tamanho dos Bins:** 
- *Poucos bins:* a curva fica mais achatada e detalhes da forma exponencial se perdem devido à baixa restrição.
- *Bins demais:* causam forte flutuação estatística em cada bin, deixando o histograma ruidoso e tornando mais complicado de interpretar e diferenciar os dados.
- *Justificativa:* A escolha de $N_{\text{bins}} \sim \sqrt{N}$ (no código, $50$ bins para $N \approx 1000$ dados) ou a regra de Freedman-Diaconis garante que cada bin tenha uma contagem estatística suficiente ($N_i \gtrsim 10$), onde a aproximação Gaussiana para as incertezas de Poisson é válida.
**Escolha da PDF Teórica:** 
A **Distribuição Exponencial** $f(t; \tau) = \frac{1}{\tau} e^{-t/\tau}$.
- *Justificativa Física:* O tempo de decaimento de uma partícula é bem descrito por uma distribuição exponencial como consequência da taxa de decaimento constante por unidade de tempo, processo estocástico de Poisson sem memória.

---

## Problema 2: PDF Exponencial e Probabilidade
**Efeito do Parâmetro $\tau$:**
- Para $\tau$ maior, o decaimento é mais lento (exponencial fica mais "achatada") e a cauda da distribuição se estende para valores maiores de $t$.
- Para $\tau$ menor, o decaimento é rápido e concentrado próximo de $t = 0$.
**Cálculo da Probabilidade $P(t \le 1.0\text{ s})$ para $\tau = 2.0\text{ s}$:**
$$P(t \le 1.0) = \int_{0}^{1} \frac{1}{2.0} e^{-t/2.0} \, dt = 1 - e^{-1/2} \approx 0.3935 \quad (39.35\%)$$

---

## Problema 3: Função de Verossimilhança
**Derivação e Máximo:**
Para $N$ medidas independentes, a verossimilhança é $L(\tau) = \frac{1}{\tau^N} \exp\left( -\frac{1}{\tau} \sum t_i \right)$. Resolvendo $dL/d\tau=0$, o estimador máximo é a média amostral: $\hat{\tau} = \frac{1}{N} \sum t_i$. Para uma medida única ($t_1 = 1.0$ s), o máximo de $L(\tau)$ ocorre em $\tau = 1.0$ s.

**Problema Numérico em Potencial:**
Para um experimento com $N$ grande, o produto direto de muitas probabilidades resulta em valores infinitesimais, causando **underflow numérico** na máquina. Por isso, converte-se o problema para a log-verossimilhança ($\ln L$).

---

## Problema 4 e 5: Log-Verossimilhança e Ajuste Numérico
**1. Tipo de Ajuste:**
O ajuste realizado é não binado. A função $-2\ln L(\tau)$ avalia diretamente a soma dos tempos individuais medidos ($\sum t_i$), ignorando contagens juntas em histogramas.

**2. Cálculo de Incertezas Numéricas:**
As incertezas de $\hat{\tau}$ são encontradas determinando pontos onde a curva de $-2\ln L(\tau)$ cruza o valor mínimo acrescido de 1.0 unidade, correspondendo ao intervalo de $1\sigma$
---

## Problema 6: Distribuições Gaussianas e Física de Partículas
**Efeito de $\mu$ e $\sigma$:**
- $\mu$ desloca horizontalmente o centro da distribuição no eixo $x$.
- $\sigma$ altera a largura e a altura da curva, mantendo a área total normalizada em 1.
**Probabilidades para $X \sim \text{Gauss}(\mu = 200\text{ GeV}, \sigma = 2\text{ GeV})$:**
1. $P(m \ge 205\text{ GeV})$ ($2.5\sigma$ acima da média):
  $$P(m \ge 205) = \int_{205}^{\infty} \text{Gauss}(x; 200, 2) \, dx \approx 0.0062 \quad (0.62\%)$$
2. $P(\text{duas partículas independentes com } m \ge 203\text{ GeV cada})$ ($1.5\sigma$ acima da média):
  $$P(m \ge 203) = \int_{203}^{\infty} \text{Gauss}(x; 200, 2) \, dx \approx 0.0668 \quad (6.68\%)$$
  $$P(\text{ambas} \ge 203) = (0.0668)^2 \approx 0.0045 \quad (0.45\%)$$

---

## Problema 7: Teorema Central do Limite (TCL)
- Para $N = 3$, o histograma do valor médio $\bar{x} = \frac{1}{3}(x_1 + x_2 + x_3)$ ainda é visivelmente assimétrico, lembrando a forma de uma distribuição exponencial.
- À medida que $N$ cresce, a distribuição de $\bar{x}$ converge para uma forma simétrica em sino, demonstrando o Teorema Central do Limite.