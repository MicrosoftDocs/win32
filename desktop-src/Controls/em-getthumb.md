---
title: EM_GETTHUMB message (Winuser.h)
description: Gets the position of the scroll box (thumb) in the vertical scroll bar of a multiline edit control. You can send this message to either an edit control or a rich edit control.
ms.assetid: 04bd0102-1652-405b-8c42-50e138abaf75
keywords:
- EM_GETTHUMB message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETTHUMB
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETTHUMB message

Gets the position of the scroll box (thumb) in the vertical scroll bar of a multiline edit control. You can send this message to either an edit control or a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

The return value is the position of the scroll box.

## Remarks

**Rich Edit:** Supported in Microsoft Rich Edit 2.0 and later. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



 

 





