---
title: Namespaces
description: Objects that reside within a given namespace are identified by a unique name.
ms.assetid: d42b4b18-d38f-4071-8e3e-9b9b71d46d4b
ms.tgt_platform: multiple
keywords:
- namespaces ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Namespaces

Objects that reside within a given namespace are identified by a unique name. For example, files stored on a PC disk drive reside in the file system namespace. The unique name of a file is based on where it is stored in the file system namespace. For example:


```C++
C:\public\documents\adsi\adsi_spec.doc
```



Directory service namespaces also identify the objects they contain by unique names which are usually based on the location in the directory where the object can be found. For example, in an X.500 directory, a given object might have a name like this:


```C++
CN=John,OU=Marketing,O=Fabrikam
```



Different directory services use different forms for naming the objects they contain. This makes dealing with different namespaces challenging, especially for developers, considering all of the different environments on which the code might be running.

A goal of Active Directory Service Interfaces (ADSI) is to provide a naming framework that allows access to namespaces of different directory service providers.

ADSI defines a naming convention that can uniquely identify an object in a heterogeneous environment. These names are called ADsPath strings. ADsPath strings take several forms:


```C++
"ADs://"
 
"LDAP://"
 
"WinNT://"
```



Additional ADsPath formats can be introduced by different ADSI providers (such as the ADSI provider for the Internet Information Services server, which support the "IIS://" ADsPaths).

 

 




