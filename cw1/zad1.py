import json
import re

with open(r"C:\Users\bartoszstaron\Desktop\Studia\3_rok\6_semestr\python_geo\cw1\teksty.json", "r") as file:
    content=file.read()

plik=json.loads(content)
teksty=str(plik.values())
teksty=teksty.lower()
teksty=teksty.split(" ")
for idx, el in enumerate(teksty):
    teksty[idx]=el.replace(".", "")
for idx, el in enumerate(teksty):
    teksty[idx]=el.replace(",", "")
print(teksty)
teksty={el[: -1]+el[-1].upper() for el in teksty}
print(teksty)