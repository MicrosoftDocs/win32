---
description: Sent to an extension DLL when the user selects a file name in the File Manager directory window or Search Results window.
title: FMEVENT_SELCHANGE message (Wfext.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FMEVENT_SELCHANGE
api_type: 
- HeaderDef
api_location: 
- Wfext.h
ms.assetid: 0773aa74-adf2-4e90-aead-2a9a981be3cb

---

# FMEVENT\_SELCHANGE message

Sent to an extension DLL when the user selects a file name in the File Manager directory window or Search Results window.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

An extension DLL should return zero if it processes this message.

## Remarks

Changes in the tree portion of the directory window do not produce this message.

Because the user can change the selection many times, the extension DLL must return promptly after processing this message to avoid slowing the selection process for the user.

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

 

 




