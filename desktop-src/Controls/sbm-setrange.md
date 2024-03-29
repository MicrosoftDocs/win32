---
title: SBM_SETRANGE message (Winuser.h)
description: The SBM\_SETRANGE message is sent to set the minimum and maximum position values for the scroll bar control.
ms.assetid: 9cf84354-3944-4c10-9b59-39427b840868
keywords:
- SBM_SETRANGE message Windows Controls
topic_type:
- apiref
api_name:
- SBM_SETRANGE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SBM\_SETRANGE message

The **SBM\_SETRANGE** message is sent to set the minimum and maximum position values for the scroll bar control.

Applications should not send this message directly. Instead, they should use the [**SetScrollRange**](/windows/desktop/api/Winuser/nf-winuser-setscrollrange) function. A window receives this message through its [*WindowProc*](/windows/win32/api/winuser/nc-winuser-wndproc) function. Applications which implement a custom scroll bar control must respond to these messages for the **SetScrollRange** function to work properly.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the minimum scrolling position.

</dd> <dt>

*lParam* 
</dt> <dd>

Specifies the maximum scrolling position.

</dd> </dl>

## Return value

**ComCtl32.dll version 5.0**: If the position of the scroll box changed, the return value is the previous position of the scroll box; otherwise, it is zero.

**ComCtl32.dll version 6.0**: The current position of the scroll box, regardless of whether it has changed.

## Remarks

The default minimum and maximum position values are zero. The difference between the values specified by the *wParam* and *lParam* parameters must not be greater than MAXLONG.

If the minimum and maximum position values are equal, the scroll bar control is hidden and, in effect, disabled.

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

[**SBM\_SETPOS**](sbm-setpos.md)
</dt> <dt>

[**SBM\_SETRANGEREDRAW**](sbm-setrangeredraw.md)
</dt> </dl>

 

