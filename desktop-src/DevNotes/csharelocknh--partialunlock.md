---
Description: 'Releases a partial lock so that other exclusive or partial lock acquirers can now enter.'
ms.assetid: '95a3e0d1-4e8b-4e30-b4fd-709b9db465de'
title: 'CShareLockNH::PartialUnlock method'
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                     |
|----------------|-------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Rwnh.dll</dt> </dl> |



 

 




