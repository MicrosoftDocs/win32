---
Description: 'Changes a shared lock to a partial lock.'
ms.assetid: '82122671-b0bd-47ad-9a25-ee8ebd3779be'
title: 'CShareLockNH::SharedToPartial method'
---

# CShareLockNH::SharedToPartial method

Changes a shared lock to a partial lock.

## Syntax


```C++
BOOL SharedToPartial();
```



## Parameters

This method has no parameters.

## Return value

Returns **TRUE** if the partial lock is obtained; otherwise, it returns **FALSE** and the lock remains in shared mode.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                     |
|----------------|-------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Rwnh.dll</dt> </dl> |



 

 




