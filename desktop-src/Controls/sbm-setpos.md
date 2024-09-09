---
title: SBM_SETPOS message (Winuser.h)
description: The SBM\_SETPOS message is sent to set the position of the scroll box (thumb) and, if requested, redraw the scroll bar to reflect the new position of the scroll box.
ms.assetid: 6b3c16ba-1cdf-41ff-8546-ba98477af334
keywords:
- SBM_SETPOS message Windows Controls
topic_type:
- apiref
api_name:
- SBM_SETPOS
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SBM\_SETPOS message

The **SBM\_SETPOS** message is sent to set the position of the scroll box (thumb) and, if requested, redraw the scroll bar to reflect the new position of the scroll box.

Applications should not send this message directly. Instead, they should use the [**SetScrollPos**](/windows/desktop/api/Winuser/nf-winuser-setscrollpos) function. A window receives this message through its [*WindowProc*](/windows/win32/api/winuser/nc-winuser-wndproc) function. Applications which implement a custom scroll bar control must respond to these messages for the **SetScrollPos** function to work properly.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the new position of the scroll box. It must be within the scrolling range. If this parameter is outside of the scrolling range, the value is rounded up or down to the nearest valid value.

</dd> <dt>

*lParam* 
</dt> <dd>

Specifies whether the scroll bar should be redrawn to reflect the new scroll box position. If this parameter is **TRUE**, the scroll bar is redrawn. If it is **FALSE**, the scroll bar is not redrawn.

</dd> </dl>

## Return value

**ComCtl32.dll version 5.0**: If the position of the scroll box changed, the return value is the previous position of the scroll box; otherwise, it is zero.

**ComCtl32.dll version 6.0**: The current position of the scroll box, regardless of whether it has changed.

## Remarks

If the scroll bar control is redrawn by a subsequent call to another function, setting the *lParam* parameter to **FALSE** is useful.

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

[**SBM\_GETPOS**](sbm-getpos.md)
</dt> <dt>

[**SBM\_GETRANGE**](sbm-getrange.md)
</dt> <dt>

[**SBM\_SETRANGE**](sbm-setrange.md)
</dt> <dt>

[**SBM\_SETRANGEREDRAW**](sbm-setrangeredraw.md)
</dt> </dl>

 

