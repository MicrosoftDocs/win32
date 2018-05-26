---
Description: Obtains a lock exclusively if no others are currently hold it.
ms.assetid: d655b89c-f2c8-4965-a21b-f539b1598296
title: CShareLockNHTryExclusiveLock method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CShareLockNH::TryExclusiveLock method

Obtains a lock exclusively if no others are currently hold it.

## Syntax


```C++
BOOL TryExclusiveLock();
```



## Parameters

This method has no parameters.

## Return value

Returns **TRUE** if the function succeeds; otherwise, it returns **FALSE**.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                     |
|----------------|-------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Rwnh.dll</dt> </dl> |



 

 




