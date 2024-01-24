---
description: Obtains a lock exclusively if no others are currently hold it.
ms.assetid: d655b89c-f2c8-4965-a21b-f539b1598296
title: CShareLockNH::TryExclusiveLock method
ms.topic: reference
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|-------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Rwnh.dll</dt> </dl> |



 

 
