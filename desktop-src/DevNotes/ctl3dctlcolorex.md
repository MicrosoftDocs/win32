---
Description: Handles the WM\_CTLCOLOR message for applications that use CTL3D.
ms.assetid: 8626a559-4856-4e7d-bf9c-edc48613b8f4
title: Ctl3dCtlColorEx function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                        |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ctl3d32.dll</dt> </dl> |



 

 




