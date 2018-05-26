---
Description: Obtains a shared lock.
ms.assetid: dff9a842-573a-4530-820d-6fd9001e502a
title: CShareLockNHShareLock method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CShareLockNH::ShareLock method

Obtains a shared lock.

## Syntax


```C++
void ShareLock();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Each call to **ShareLock** must be paired with exactly one call to [**ShareUnlock**](csharelocknh--shareunlock.md). Only a thread that successfully calls **ShareLock** can call **ShareUnlock**; otherwise, a deadlock can occur.

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                     |
|----------------|-------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Rwnh.dll</dt> </dl> |



## See also

<dl> <dt>

[**ShareUnlock**](csharelocknh--shareunlock.md)
</dt> </dl>

 

 




