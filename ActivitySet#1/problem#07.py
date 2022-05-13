# Strings

text = "X-DSPAM-Confidence:    0.8475"
pos=text.find('    ')
piece=text[pos:]
result=float(piece)
print(result)