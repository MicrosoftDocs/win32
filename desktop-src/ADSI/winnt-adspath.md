---
title: WinNT ADsPath
description: This topic contains examples of strings to use for the WinNT ADsPath.
ms.assetid: 0fad4b34-5287-43a0-a172-a08955b8b132
ms.tgt_platform: multiple
keywords:
- WinNT service provider ADSI , WinNT ADsPath
- ADsPath ADSI , WinNT, description
ms.topic: article
ms.date: 05/31/2018
---

# WinNT ADsPath

The ADsPath string for the ADSI WinNT provider can be one of the following forms:


```C++
WinNT:
WinNT://<domain name>
WinNT://<domain name>/<server>
WinNT://<domain name>/<path>
WinNT://<domain name>/<object name>
WinNT://<domain name>/<object name>,<object class>
WinNT://<server>
WinNT://<server>/<object name>
WinNT://<server>/<object name>,<object class>
```



The domain name can be either a NETBIOS name or a DNS name.

The server is the name of a specific server within the domain.

The path is the path of on object, such as "printserver1/printer2".

The object name is the name of a specific object.

The object class is the class name of the named object. One example of this usage would be "WinNT://MyServer/JeffSmith,user". Specifying a class name can improve the performance of the bind operation.

 

 




