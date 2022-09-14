---
title: EM_SETREADONLY message (Winuser.h)
description: Sets or removes the read-only style (ES\_READONLY) of an edit control. You can send this message to either an edit control or a rich edit control.
ms.assetid: a10b3f57-0e67-4a0f-89f3-9c8ebd1514f8
keywords:
- EM_SETREADONLY message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETREADONLY
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETREADONLY message

Sets or removes the read-only style ([**ES\_READONLY**](edit-control-styles.md)) of an edit control. You can send this message to either an edit control or a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies whether to set or remove the [**ES\_READONLY**](edit-control-styles.md) style. A value of **TRUE** sets the **ES\_READONLY** style; a value of **FALSE** removes the **ES\_READONLY** style.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

If the operation succeeds, the return value is nonzero.

If the operation fails, the return value is zero.

## Remarks

When an edit control has the [**ES\_READONLY**](edit-control-styles.md) style, the user cannot change the text within the edit control.

To determine whether an edit control has the [**ES\_READONLY**](edit-control-styles.md) style, use the [**GetWindowLong**](/windows/desktop/api/winuser/nf-winuser-getwindowlonga) function with the GWL\_STYLE flag.

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**GetWindowLong**](/windows/desktop/api/winuser/nf-winuser-getwindowlonga)
</dt> </dl>

 

