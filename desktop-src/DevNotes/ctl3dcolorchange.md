---
Description: Handles system color changes for applications that use CTL3D.
ms.assetid: b1eadb7d-39a5-47e9-9ae5-62bd33557f6b
title: Ctl3dColorChange function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Ctl3dColorChange
api_type: 
- DllExport
api_location: 
- Ctl3d32.dll
---

# Ctl3dColorChange function

Handles system color changes for applications that use CTL3D.

## Syntax


```C++
BOOL Ctl3dColorChange(void);
```



## Parameters

This function has no parameters.

## Return value

Returns **TRUE** if the function succeeds; otherwise, it returns **FALSE**.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions.

This function should be called in the application's main window procedure for the **WM\_SYSCOLORCHANGE** message, as shown below.

## Examples

``` syntax
case WM_SYSCOLORCHANGE:
   Ctl3dColorChange();
   break;
```

## Requirements



|                |                                                                                        |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ctl3d32.dll</dt> </dl> |



 

 




