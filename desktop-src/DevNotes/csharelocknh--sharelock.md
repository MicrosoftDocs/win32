---
description: Obtains a shared lock.
ms.assetid: dff9a842-573a-4530-820d-6fd9001e502a
title: CShareLockNH::ShareLock method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CShareLockNH.ShareLock
api_type: 
- COM
api_location: 
- Rwnh.dll
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|-------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Rwnh.dll</dt> </dl> |



## See also

<dl> <dt>

[**ShareUnlock**](csharelocknh--shareunlock.md)
</dt> </dl>

 

 
