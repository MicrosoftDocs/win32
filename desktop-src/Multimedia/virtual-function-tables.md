---
title: Virtual Function Tables
description: Virtual Function Tables
ms.assetid: 1b7c6da6-3156-46fe-a9ca-0c1717fe28b5
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Virtual Function Tables

\[The feature associated with this page, [Custom File and Stream Handlers](/windows/win32/multimedia/custom-file-and-stream-handlers), is a legacy feature. It has been superseded by [MediaStreamSource class](/uwp/api/Windows.Media.Core.MediaStreamSource). **MediaStreamSource class** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaStreamSource class** instead of **Custom File and Stream Handlers**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A virtual function table is an array of pointers to the methods an object supports. If you're using C, an object appears as a structure whose first member is a pointer to the virtual function table (**lpVtbl**); that is, the first member points to an array containing function pointers. The methods all take a pointer to the function table as the first parameter. Thus, the following example calls the **Read** method of a **pStream** object:


```C++
pStream->lpVtbl->Read(pStream, parameters) 
 
```



In C+ +, the pointer to the virtual function table, the *this* pointer, is implicit. The following is equivalent to the previous example when using C+ +:


```C++
pStream->Read(parameters) 
 
```



 

 




