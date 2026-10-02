cmr=int(input("current month reading: "))
pmr=int(input("previous month reading:"))
nu=cmr-pmr
bill=7.45*nu
print()
print("="*35)
print("         ELECTRICAL BILL ")
print("="*35)
print("CMR: ",cmr)
print("PMR: ",pmr)
print("Units : ",nu)
print("Bill: ",bill)
print("="*35)