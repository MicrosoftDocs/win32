---
Description: Indicates the version of CTL3D that is currently running.
ms.assetid: 38c0842c-417f-4ca1-acc2-3bbadf45c804
title: Ctl3dGetVer function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Ctl3dGetVer
api_type: 
- DllExport
api_location: 
- Ctl3d32.dll
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions.

## Requirements



|                |                                                                                        |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ctl3d32.dll</dt> </dl> |



 

 




