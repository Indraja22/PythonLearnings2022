def whoCanDrive(*driverAgeList):
   for driverAge in driverAgeList:
        if(driverAge > 18):
            print("You can drive!", driverAge)
        else:
            print("You cannot drive!!!", driverAge)

# driverAgesList=[11,34,23,56,77,27,31,20]
whoCanDrive(11,23,44,55,21,66,31)