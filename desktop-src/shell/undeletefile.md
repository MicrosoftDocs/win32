---
description: Specifies an application-defined callback function called by File Manager when the user chooses the Undelete command from the File menu.
title: FM_UNDELETE_PROC function pointer (Wfext.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FM_UNDELETE_PROC
api_type: 
- UserDefined
api_location: 
- Wfext.h
ms.assetid: 456b053e-e83d-43af-9691-57e1d4fd3f8f

---

# FM\_UNDELETE\_PROC function pointer

Specifies an application-defined callback function called by File Manager when the user chooses the **Undelete** command from the **File** menu.

## Syntax


```C++
typedef DWORD ( APIENTRY *FM_UNDELETE_PROC)(
   HWND  hwndOwner,
   LPSTR lpszDir
);
```



## Parameters

<dl> <dt>

*hwndOwner* 
</dt> <dd>

Type: **HWND**

The window handle to File Manager. An undelete DLL should use this handle to specify the owner window for any dialog box or message box the DLL might display.

</dd> <dt>

*lpszDir* 
</dt> <dd>

Type: **LPSTR**

The address of a null-terminated string that contains the name of the initial directory.

</dd> </dl>

## Return value

Type: **DWORD**

Returns one of the following values.



| Return code                                                                             | Description                                                        |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**-1**</dt> </dl>       | An error occurred.<br/>                                      |
| <dl> <dt>**IDOK**</dt> </dl>     | A file was undeleted. File Manager repaints its window.<br/> |
| <dl> <dt>**IDCANCEL**</dt> </dl> | No file was undeleted.<br/>                                  |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wfext.h</dt> </dl> |



 

 




