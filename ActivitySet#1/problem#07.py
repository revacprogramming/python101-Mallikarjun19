# Strings

text = "X-DSPAM-Confidence:    0.8475"
pos=text.find(':')
print(pos)
piece=text[pos+4:]
result=float(piece)
print(result)