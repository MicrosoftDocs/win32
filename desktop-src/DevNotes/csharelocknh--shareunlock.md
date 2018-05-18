---
Description: 'Releases a shared lock.'
ms.assetid: 'c2e9eb68-aacb-4196-b09e-d2748efb7fd6'
title: 'CShareLockNH::ShareUnlock method'
---

# CShareLockNH::ShareUnlock method

Releases a shared lock.

## Syntax


```C++
void ShareUnlock();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Each call to [**ShareLock**](csharelocknh--sharelock.md) must be paired with exactly one call to **ShareUnlock**. Only a thread that successfully calls **ShareLock** can call **ShareUnlock**; otherwise, a deadlock can occur.

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                     |
|----------------|-------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Rwnh.dll</dt> </dl> |



## See also

<dl> <dt>

[**ShareLock**](csharelocknh--sharelock.md)
</dt> </dl>

 

 




