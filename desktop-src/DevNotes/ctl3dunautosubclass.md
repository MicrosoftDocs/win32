---
Description: Turns off automatic subclassing.
ms.assetid: 85e5689f-6805-4aad-b97c-aa496e315900
title: Ctl3dUnAutoSubclass function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Ctl3dUnAutoSubclass
api_type: 
- DllExport
api_location: 
- Ctl3d32.dll
---

# Ctl3dUnAutoSubclass function

Turns off automatic subclassing.

## Syntax


```C++
BOOL Ctl3dUnAutoSubclass(void);
```



## Parameters

This function has no parameters.

## Return value

Returns **TRUE** if the function succeeds; otherwise, it returns **FALSE**.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions.

## Requirements



|                |                                                                                        |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ctl3d32.dll</dt> </dl> |



 

 




