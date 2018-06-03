---
title: Array Definitions
description: MIDL accepts both fixed-size arrays and arrays declared as SAFEARRAY.
ms.assetid: fe66fdbc-0de2-4b0d-9723-2f6d07e534cd
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Array Definitions

MIDL accepts both fixed-size arrays and arrays declared as SAFEARRAY.

Use a C-style syntax for a fixed size array:


```C++
<type> <arrname>[<size>];
```



To describe a SAFEARRAY, use the following syntax:


```C++
SAFEARRAY (<elementtype>) *<arrayname>
```



A function returning a SAFEARRAY has the following syntax:


```C++
SAFEARRAY (<elementtype>) <myfunction>(<parameterlist>);
```



 

 




