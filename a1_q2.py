marks=int(input("Enter marks :"))
if marks>90:
  print("EXCELLENT")
elif marks>80 and marks<=90:
  print("GOOD")
elif marks>70 and marks<=80:
  print("FAIR")
elif marks>60 and marks<=70:
  print("MEETS EXPECTATIONS")
else:
  print("BELOW PAR")
