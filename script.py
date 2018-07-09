#!/usr/bin/python3

soal = input("Enter the morse to decode: ")

sandi = {
  "10": "A",
  "0111": "B",
  "0101": "C",
  "011": "D",
  "1": "E",
  "1101": "F",
  "001": "G",
  "1111": "H",
  "11": "I",
  "1000": "J",
  "010": "K",
  "1011": "L",
  "00": "M",
  "01": "N",
  "000": "O",
  "1001": "P",
  "0010": "Q",
  "101": "R",
  "111": "S",
  "0": "T",
  "110": "U",
  "1110": "V",
  "100": "W",
  "0110": "X",
  "0100": "Y",
  "0011": "Z"
}

def morse(symbol):
  if symbol == '-':
    return "0"
  elif symbol == '.':
    return "1"

hasil = [[]]
cnt = 0

for i in range(len(soal)):
  if soal[i] == " ":
    hasil.append([])
    cnt += 1
  else:
    hasil[cnt].append(morse(soal[i]))

decoded = []

for j in range(len(hasil)):
  # harus dalam bentuk str agar bisa digabungkan
  temp = "".join(hasil[j])
  decoded.append(sandi[temp])

print("".join(decoded))
