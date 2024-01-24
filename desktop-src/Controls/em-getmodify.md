---
title: EM_GETMODIFY message (Winuser.h)
description: Gets the state of an edit control's modification flag. The flag indicates whether the contents of the edit control have been modified. You can send this message to either an edit control or a rich edit control.
ms.assetid: 4229e2f2-3493-4721-8b52-8933c9dc0a77
keywords:
- EM_GETMODIFY message Windows Controls
topic_type:
- apiref
api_name:
- EM_GETMODIFY
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_GETMODIFY message

Gets the state of an edit control's modification flag. The flag indicates whether the contents of the edit control have been modified. You can send this message to either an edit control or a rich edit control.

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

If the contents of edit control have been modified, the return value is nonzero; otherwise, it is zero.

## Remarks

The system automatically clears the modification flag to zero when the control is created. If the user changes the control's text, the system sets the flag to nonzero. You can send the [**EM\_SETMODIFY**](em-setmodify.md) message to the edit control to set or clear the flag.

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**EM\_SETMODIFY**](em-setmodify.md)
</dt> </dl>

 

 





