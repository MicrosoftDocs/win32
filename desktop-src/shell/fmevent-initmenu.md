---
description: Sent to an extension DLL when the user selects the menu for the extension from the File Manager menu bar. The extension can use this notification to initialize menu items.
title: FMEVENT_INITMENU message (Wfext.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FMEVENT_INITMENU
api_type: 
- HeaderDef
api_location: 
- Wfext.h
ms.assetid: 8074a09f-ad94-4a7a-8c0b-965b0f8f6334

---

# FMEVENT\_INITMENU message

Sent to an extension DLL when the user selects the menu for the extension from the File Manager menu bar. The extension can use this notification to initialize menu items.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*hmenu* 
</dt> <dd>

A handle to the File Manager menu bar.

</dd> </dl>

## Return value

An extension DLL should return zero if it processes this message.

## Remarks

An extension DLL receives this message only when the user selects the top-level menu. If the extension contains submenus, it must initialize them at the same time it initializes the top-level menu.

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

 

 




