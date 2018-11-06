---
Description: Acquires a reader/writer lock.
ms.assetid: fd212dd9-034b-4e0c-9111-e3460ea6f133
title: CShareLockNH::ExclusiveLock method
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CShareLockNH.ExclusiveLock
api_type: 
- COM
api_location: 
- Rwnh.dll
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions.

## Requirements



|                |                                                                                     |
|----------------|-------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Rwnh.dll</dt> </dl> |



## See also

<dl> <dt>

[**ExclusiveUnlock**](csharelocknh--exclusiveunlock.md)
</dt> </dl>

 

 




