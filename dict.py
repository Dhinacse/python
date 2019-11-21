sample =	{
  "name": "ram",
  "dept": "cse",
  "year": "final"
}
sample["college"] = "anna university"
print(sample)


details={"ram":"final year", "ravi": "third year"}
for name,year in details.items():
  print(name+"studies"+year)
