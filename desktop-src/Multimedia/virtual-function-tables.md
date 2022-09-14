---
title: Virtual Function Tables
description: Virtual Function Tables
ms.assetid: 1b7c6da6-3156-46fe-a9ca-0c1717fe28b5
ms.topic: article
ms.date: 05/31/2018
---

# Virtual Function Tables

A virtual function table is an array of pointers to the methods an object supports. If you're using C, an object appears as a structure whose first member is a pointer to the virtual function table (**lpVtbl**); that is, the first member points to an array containing function pointers. The methods all take a pointer to the function table as the first parameter. Thus, the following example calls the **Read** method of a **pStream** object:


```C++
pStream->lpVtbl->Read(pStream, parameters) 
 
```



In C+ +, the pointer to the virtual function table, the *this* pointer, is implicit. The following is equivalent to the previous example when using C+ +:


```C++
pStream->Read(parameters) 
 
```



 

 




