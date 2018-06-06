---
Description: Acquires a reader/writer lock.
ms.assetid: fd212dd9-034b-4e0c-9111-e3460ea6f133
title: CShareLockNH::ExclusiveLock method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                     |
|----------------|-------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Rwnh.dll</dt> </dl> |



## See also

<dl> <dt>

[**ExclusiveUnlock**](csharelocknh--exclusiveunlock.md)
</dt> </dl>

 

 




