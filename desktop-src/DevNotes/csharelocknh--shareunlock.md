---
Description: Releases a shared lock.
ms.assetid: c2e9eb68-aacb-4196-b09e-d2748efb7fd6
title: CShareLockNH::ShareUnlock method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/windows/desktop/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/windows/desktop/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                     |
|----------------|-------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Rwnh.dll</dt> </dl> |



## See also

<dl> <dt>

[**ShareLock**](csharelocknh--sharelock.md)
</dt> </dl>

 

 




