---
title: EM_SCROLLCARET message (Winuser.h)
description: Scrolls the caret into view in an edit control. You can send this message to either an edit control or a rich edit control.
ms.assetid: 7a33034d-9369-49f8-a881-0c1d2cedff6a
keywords:
- EM_SCROLLCARET message Windows Controls
topic_type:
- apiref
api_name:
- EM_SCROLLCARET
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SCROLLCARET message

Scrolls the caret into view in an edit control. You can send this message to either an edit control or a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is reserved. It should be set to zero.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is reserved. It should be set to zero.

</dd> </dl>

## Return value

The return value is not meaningful.

## Remarks

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EM\_LINESCROLL**](em-linescroll.md)
</dt> <dt>

[**EM\_SCROLL**](em-scroll.md)
</dt> <dt>

[**WM\_VSCROLL**](wm-vscroll.md)
</dt> </dl>

 

 





