---
Description: Releases a partial lock so that other exclusive or partial lock acquirers can now enter.
ms.assetid: 95a3e0d1-4e8b-4e30-b4fd-709b9db465de
title: CShareLockNH::PartialUnlock method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions.

## Requirements



|                |                                                                                     |
|----------------|-------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Rwnh.dll</dt> </dl> |



 

 




