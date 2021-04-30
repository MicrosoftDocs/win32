---
description: Subclasses an individual control unless the control appears in a dialog box.
ms.assetid: 07a2bce1-4c69-4f8d-bb24-b17351f5e771
title: Ctl3dSubclassCtl function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Ctl3dSubclassCtl
api_type: 
- DllExport
api_location: 
- Ctl3d32.dll
---

# Ctl3dSubclassCtl function

Subclasses an individual control unless the control appears in a dialog box.

## Syntax


```C++
BOOL Ctl3dSubclassCtl(
   HWND hwnd
);
```



## Parameters

<dl> <dt>

*hwnd* 
</dt> <dd>

A handle to the control window.

</dd> </dl>

## Return value

Returns **TRUE** if the control is successfully subclassed; otherwise, it returns **FALSE**.

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ctl3d32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Ctl3dUnsubclassCtl**](ctl3dunsubclassctl.md)
</dt> </dl>

 

 
