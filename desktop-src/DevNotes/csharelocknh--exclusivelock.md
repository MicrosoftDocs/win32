---
Description: Acquires a reader/writer lock.
ms.assetid: fd212dd9-034b-4e0c-9111-e3460ea6f133
title: CShareLockNHExclusiveLock method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CShareLockNH::ExclusiveLock method

Acquires a reader/writer lock.

## Syntax


```C++
void ExclusiveLock();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Each call to **ExclusiveLock** must be paired with exactly one call to [**ExclusiveUnlock**](csharelocknh--exclusiveunlock.md) to avoid the risk of a deadlock.

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                     |
|----------------|-------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Rwnh.dll</dt> </dl> |



## See also

<dl> <dt>

[**ExclusiveUnlock**](csharelocknh--exclusiveunlock.md)
</dt> </dl>

 

 




