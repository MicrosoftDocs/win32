---
Description: Subclasses all controls in a dialog box and in the dialog window itself.
ms.assetid: 4d3c298b-07ba-4668-badd-dddecc389e70
title: Ctl3dSubclassDlgEx function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Ctl3dSubclassDlgEx function

Subclasses all controls in a dialog box and in the dialog window itself.

## Syntax


```C++
PUBLIC BOOL FAR PASCAL Ctl3dSubclassDlgEx(
   HWND  hwndDlg,
   DWORD grbit
);
```



## Parameters

<dl> <dt>

*hwndDlg* 
</dt> <dd>

A handle to the dialog window.

</dd> <dt>

*grbit* 
</dt> <dd>

The control types to be subclassed. This value can be any of the following.



| Value                                                                                                                                                                                                                                     | Meaning                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| <span id="CTL3D_BUTTONS"></span><span id="ctl3d_buttons"></span><dl> <dt>**CTL3D\_BUTTONS**</dt> <dt>0x0001</dt> </dl>                 | Subclass buttons.<br/>                  |
| <span id="CTL3D_LISTBOXES"></span><span id="ctl3d_listboxes"></span><dl> <dt>**CTL3D\_LISTBOXES**</dt> <dt>0x0002</dt> </dl>           | Subclass list boxes.<br/>               |
| <span id="CTL3D_EDITS"></span><span id="ctl3d_edits"></span><dl> <dt>**CTL3D\_EDITS**</dt> <dt>0x0004</dt> </dl>                       | Subclass edit controls.<br/>            |
| <span id="CTL3D_COMBOS"></span><span id="ctl3d_combos"></span><dl> <dt>**CTL3D\_COMBOS**</dt> <dt>0x0008</dt> </dl>                    | Subclass combo boxes.<br/>              |
| <span id="CTL3D_STATICTEXTS"></span><span id="ctl3d_statictexts"></span><dl> <dt>**CTL3D\_STATICTEXTS**</dt> <dt>0x0010</dt> </dl>     | Subclass static text controls.<br/>     |
| <span id="CTL3D_STATICFRAMES"></span><span id="ctl3d_staticframes"></span><dl> <dt>**CTL3D\_STATICFRAMES**</dt> <dt>0x0020</dt> </dl>  | Subclass static frames.<br/>            |
| <span id="CTL3D_ALL"></span><span id="ctl3d_all"></span><dl> <dt>**CTL3D\_ALL**</dt> <dt>0xffff</dt> </dl>                             | Subclass all controls.<br/>             |
| <span id="CTL3D_NODLGWINDOW"></span><span id="ctl3d_nodlgwindow"></span><dl> <dt>**CTL3D\_NODLGWINDOW**</dt> <dt>0x00010000</dt> </dl> | Do not subclass the dialog window.<br/> |



 

</dd> </dl>

## Return value

Returns **TRUE** if the function succeeds; otherwise, it returns **FALSE**.

## Remarks

This function is especially useful in applications based on C++.

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                        |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ctl3d32.dll</dt> </dl> |



 

 




