---
description: Handles the WM\_CTLCOLOR message for applications that use CTL3D.
ms.assetid: 8626a559-4856-4e7d-bf9c-edc48613b8f4
title: Ctl3dCtlColorEx function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Ctl3dCtlColorEx
api_type: 
- DllExport
api_location: 
- Ctl3d32.dll
---

# Ctl3dCtlColorEx function

Handles the **WM\_CTLCOLOR** message for applications that use CTL3D.

## Syntax


```C++
HBRUSH Ctl3dCtlColorEx(
   UINT   wm,
   WPARAM wParam,
   LPARAM lParam
);
```



## Parameters

<dl> <dt>

*wm* 
</dt> <dd>

The **WM\_CTLCOLOR** message for the application.

</dd> <dt>

*wParam* 
</dt> <dd>

A handle to the display context (DC).

</dd> <dt>

*lParam* 
</dt> <dd>

A handle to a child window (control).

</dd> </dl>

## Return value

Returns a handle to the appropriate brush if the function succeeds; otherwise, it returns `(HBRUSH)(0)` indicating that an error occurred.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ctl3d32.dll</dt> </dl> |



 

 
