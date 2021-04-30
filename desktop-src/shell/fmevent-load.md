---
description: Sent to an extension DLL when File Manager is loading the DLL.
ms.assetid: 9d673ab8-c468-4b46-b96e-1adfaa9f85fb
title: FMEVENT_LOAD message (Wfext.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FMEVENT_LOAD
api_type: 
- HeaderDef
api_location: 
- Wfext.h
---

# FMEVENT\_LOAD message

Sent to an extension DLL when File Manager is loading the DLL.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lpfmsld* 
</dt> <dd>

The address of an [**FMS\_LOAD**](fms-load.md) structure that specifies the menu item delta value.

</dd> </dl>

## Return value

An extension DLL must return **TRUE** to continue loading the DLL. If the DLL returns **FALSE**, File Manager calls the [**FreeLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-freelibrary) function and ends any communication with the extension DLL.

## Remarks

An application should fill the **dwSize**, **szMenuName**, and **hMenu** members in the [**FMS\_LOAD**](fms-load.md) structure. It should also save the value of the **wMenuDelta** member and use it to identify menu items when modifying the menu.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wfext.h</dt> </dl> |



## See also

<dl> <dt>

[**FMExtensionProc**](fmextensionproc.md)
</dt> </dl>

 

 
