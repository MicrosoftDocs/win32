---
Description: 'Prevents more than one thread from completing acquiring a lock.'
ms.assetid: '9cdcc6d5-b2f1-4c88-b859-1c15a80e70a9'
title: 'CShareLockNH::PartialLock method'
---

# CShareLockNH::PartialLock method

Prevents more than one thread from completing acquiring a lock.

## Syntax


```C++
void PartialLock();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

While **PartialLock** is in effect, other threads calling [**ShareLock**](csharelocknh--sharelock.md) can enter the lock.

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                     |
|----------------|-------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Rwnh.dll</dt> </dl> |



 

 




