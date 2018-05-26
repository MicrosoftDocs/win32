---
title: The Hard Fault Action
description: The Hard Fault Action
ms.assetid: 1ffe3f5d-5868-421b-874e-a8f5565e9b62
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# The Hard Fault Action

The hard fault action produces a text report that summarizes the various hard faults. The usage for this action is:


```
-a hardfault [-file] [-bytes] [-range T1 T2] 
```





| Option                  | Description                                                          |
|-------------------------|----------------------------------------------------------------------|
| file <br/>        | Sort by file first, default is process major<br/>              |
| bytes <br/>       | Sort by total number of bytes, default is by fault counts<br/> |
| range T1 T2 <br/> | Show hard faults recorded between T1 and T2, in use<br/>       |



 

 

 





