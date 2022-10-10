# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 18:52:33 2022

@author: Alexander
"""

datos = 10
datos2 = 100
if datos == datos2:
    print(True)
else:
    print(False)


nativeVLAN = 100
dataVLAN = 100
if nativeVLAN == dataVLAN:
    print("The native VLAN and the data VLAN are the same.")
else:
    print("This native VLAN and the data VLAN are different.")
    

aclNum = int (input("What is the IPv4 ACL number? "))
if aclNum >= 1 and aclNum <= 99:
    print("This is a standard IPv4 ACL.")
elif aclNum >=100 and aclNum <=199:
    print("This is a extended IPv4 ACL.")
else:
    print("This is not a standard or extended IPv4 ACL.")

