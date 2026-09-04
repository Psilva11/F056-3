import re

with open("brilcalc.log", "r") as f:
  conteudo = f.read()

summary_re = re.compile(
    r"\|\s*[\d.]+\s*\|\s*[\d.]+\s*\|\s*[\d.]+\s*\|\s*[\d.]+\s*\|\s*[\d.]+\s*\|\s*(?P<totrecorded>[\d.]+)\s*\|"
)

aux = summary_re.search(conteudo)

if aux:
  totalrecorded_pb = float(aux.group("totrecorded"))
  totalrecorded_fb = totalrecorded_pb/1000
  totalrecorded_fb = round(totalrecorded_fb, 1)

  print(f"Luminosidade integrada recorded: ", totalrecorded_fb, "fb^-1")