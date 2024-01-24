---
description: Releases a partial lock so that other exclusive or partial lock acquirers can now enter.
ms.assetid: 95a3e0d1-4e8b-4e30-b4fd-709b9db465de
title: CShareLockNH::PartialUnlock method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CShareLockNH.PartialUnlock
api_type: 
- COM
api_location: 
- Rwnh.dll
---

# CShareLockNH::PartialUnlock method

Releases a partial lock so that other exclusive or partial lock acquirers can now enter.

## Syntax


```C++
void PartialUnlock();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|-------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Rwnh.dll</dt> </dl> |



 

 
