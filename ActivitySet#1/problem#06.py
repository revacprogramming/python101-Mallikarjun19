# Loops & Iterators

largest = None
smallest = None

while True:
    num = input("Enter a number:")
    if num == "done":
        break
    try:
      x=int(num)
    except:
      print("invalid input")
      continue
    if largest is None:
      largest = x
    if smallest is None:
      smallest= x
    if x < smallest:
      smallest = x
    elif x > largest:
      largest = x

def done(largest,smallest):
  print("Maximum", largest)
  print("Minimum",smallest)

done(largest,smallest)
