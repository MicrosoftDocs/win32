---
title: Enumeration
description: Accessing and Manipulating Data with ADSI provides several examples of enumeration. You can also enumerate the children of container objects. These children are objects themselves, rather than just properties on objects.
ms.assetid: 1db19b00-8e43-4fc0-9099-1a1135219600
ms.tgt_platform: multiple
keywords:
- ADSI ADSI ,example code Visual Basic ,using IADsContainer to enumerate objects
- containers ADSI ,using IADsContainer to enumerate children of container
ms.topic: article
ms.date: 05/31/2018
---

# Enumeration

[Accessing and Manipulating Data with ADSI](accessing-and-manipulating-data-with-adsi.md) provides several examples of enumeration. You can also enumerate the children of container objects. These children are objects themselves, rather than just properties on objects.

The following example uses the [**IADsContainer**](/windows/desktop/api/Iads/nn-iads-iadscontainer) interface to enumerate the children of the container.


```VB
Dim Container as IADsContainer
Dim Child as IADs

Set Container = GetObject("LDAP://MyServer/DC=MyDomain,DC=Fabrikam,DC=com")
 
For Each Child in Container
     Debug.Print Child.Name
Next Child
```



 

 




