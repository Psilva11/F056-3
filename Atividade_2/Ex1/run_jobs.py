import multiprocessing as mp
import subprocess

def eventloop(i):
  with open(f"output_{i}.txt", "w") as arquivo:
    subprocess.run(["./hello", str(i)], stdout = arquivo)

if __name__ == "__main__":
  processos = []

  for i in range(1,11):
    p = mp.Process(target=eventloop, args=(i,))
    p.start()
    processos.append(p)

  for p in processos:
    p.join()

  print("Jobs finalizados!")