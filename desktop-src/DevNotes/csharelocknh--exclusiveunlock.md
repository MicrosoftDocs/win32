---
Description: 'Releases a lock acquired by using ExclusiveLock to shared mode.'
ms.assetid: 'd38354f0-2eb3-4924-99b5-1331e587ce32'
title: 'CShareLockNH::ExclusiveUnlock method'
---

# CShareLockNH::ExclusiveUnlock method

Releases a lock acquired by using [**ExclusiveLock**](csharelocknh--exclusivelock.md) to shared mode.

## Syntax


```C++
void ExclusiveUnlock();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Each call to [**ExclusiveLock**](csharelocknh--exclusivelock.md) must be paired with exactly one call to **ExclusiveUnlock** to avoid the risk of a deadlock.

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                     |
|----------------|-------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Rwnh.dll</dt> </dl> |



## See also

<dl> <dt>

[**ExclusiveLock**](csharelocknh--exclusivelock.md)
</dt> </dl>

 

 




