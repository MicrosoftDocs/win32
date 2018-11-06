---
Description: Verifies whether controls can use 3D effects.
ms.assetid: fb7b892f-2580-41ac-b2ef-938da3cc1dc2
title: Ctl3dEnabled function
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Ctl3dEnabled
api_type: 
- DllExport
api_location: 
- Ctl3d32.dll
---

# Ctl3dEnabled function

Verifies whether controls can use 3D effects.

## Syntax


```C++
BOOL Ctl3dEnabled(void);
```



## Parameters

This function has no parameters.

## Return value

Returns **TRUE** if controls can use 3D effects; otherwise, it returns **FALSE**.

## Remarks

In Windows 4.0 or later, **Ctl3dEnabled** and [**Ctl3dRegister**](ctl3dregister.md) return **FALSE**.

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions.

## Requirements



|                |                                                                                        |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ctl3d32.dll</dt> </dl> |



 

 




