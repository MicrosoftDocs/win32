---
title: GUIDs and the System Registry
description: The system registry is a central repository that contains information about objects.
ms.assetid: 'a3ecd640-015b-4e90-bc3b-03df16d53118'
---

# GUIDs and the System Registry

The system registry is a central repository that contains information about objects. GUIDs are used to index that information. You can view the registration information on your system by running Regedit.exe with the **/v** option:


```C++
regedit /v 
```



Typically, a name is connected with a GUID (for example, Hello.Application maps to a GUID), and the GUID is connected to all the other relevant aspects of the object (for example, the GUID maps to Hello.exe).

GUIDs are created with the tool Guidgen.exe. Running Guidgen.exe produces a very large hexidecimal number that uniquely identifies an object, whether it is a class, interface, library, or some other type of object.

 

 




