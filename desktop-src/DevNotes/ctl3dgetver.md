---
Description: 'Indicates the version of CTL3D that is currently running.'
ms.assetid: '38c0842c-417f-4ca1-acc2-3bbadf45c804'
title: Ctl3dGetVer function
---

# Ctl3dGetVer function

Indicates the version of CTL3D that is currently running.

## Syntax


```C++
WORD Ctl3dGetVer(void);
```



## Parameters

This function has no parameters.

## Return value

Returns a value that contains the major version number in the high-order byte and the minor version number in the low-order byte.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                        |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ctl3d32.dll</dt> </dl> |



 

 




