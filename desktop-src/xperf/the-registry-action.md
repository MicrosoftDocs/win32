---
title: The Registry Action
description: The Registry Action
ms.assetid: 40f7be04-cfcf-4945-96db-48c32aeca464
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# The Registry Action

The registry action produces a text file that summarizes the various metrics regarding registry accesses and manipulations. The usage for this action is:


```
-a registry [-counts [n] -tree -unknown -range T1 T2] 
```





| Option                   | Description                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------|
| counts \[n\] <br/> | Print out Registry access statistics for *n* use intervals. If the interval is not specified, default is 1<br/> |
| range T1 T2 <br/>  | Show delays between T1 and T2, in use<br/>                                                                      |



 

If no option is specified, default is -counts 1.

 

 





