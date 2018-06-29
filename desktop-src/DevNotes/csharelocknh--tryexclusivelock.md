---
Description: Obtains a lock exclusively if no others are currently hold it.
ms.assetid: d655b89c-f2c8-4965-a21b-f539b1598296
title: CShareLockNH::TryExclusiveLock method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CShareLockNH.TryExclusiveLock
api_type: 
- COM
api_location: 
- Rwnh.dll
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions.

## Requirements



|                |                                                                                     |
|----------------|-------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Rwnh.dll</dt> </dl> |



 

 




