---
Description: Sent to an extension DLL when File Manager is loading its toolbar. This message allows an extension DLL to add a button to the File Manager toolbar.
title: FMEVENT\_TOOLBARLOAD message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FMEVENT_TOOLBARLOAD
api_type: 
- HeaderDef
api_location: 
- Wfext.h
---

# FMEVENT\_TOOLBARLOAD message

Sent to an extension DLL when File Manager is loading its toolbar. This message allows an extension DLL to add a button to the File Manager toolbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lpfmstbl* 
</dt> <dd>

The address of an [**FMS\_TOOLBARLOAD**](fms-toolbarload.md) structure. If the extension DLL adds a button to the toolbar in File Manager, the DLL should fill the structure with information about the button.

</dd> </dl>

## Return value

An extension DLL must return **TRUE** to add the button to the toolbar. If the DLL returns **FALSE**, File Manager does not add the button.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wfext.h</dt> </dl> |



## See also

<dl> <dt>

[**FMExtensionProc**](fmextensionproc.md)
</dt> </dl>

 

 




