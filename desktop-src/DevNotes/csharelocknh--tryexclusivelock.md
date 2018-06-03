---
Description: Obtains a lock exclusively if no others are currently hold it.
ms.assetid: d655b89c-f2c8-4965-a21b-f539b1598296
title: CShareLockNH::TryExclusiveLock method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/windows/desktop/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/windows/desktop/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                     |
|----------------|-------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Rwnh.dll</dt> </dl> |



 

 




