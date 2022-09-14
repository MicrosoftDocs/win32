---
description: Changes a shared lock to a partial lock.
ms.assetid: 82122671-b0bd-47ad-9a25-ee8ebd3779be
title: CShareLockNH::SharedToPartial method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CShareLockNH.SharedToPartial
api_type: 
- COM
api_location: 
- Rwnh.dll
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|-------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Rwnh.dll</dt> </dl> |



 

 
