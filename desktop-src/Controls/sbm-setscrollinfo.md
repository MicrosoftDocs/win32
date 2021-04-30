---
title: SBM_SETSCROLLINFO message (Winuser.h)
description: The SBM\_SETSCROLLINFO message is sent to set the parameters of a scroll bar.
ms.assetid: e0e42a81-67be-4d40-88c8-77398b068617
keywords:
- SBM_SETSCROLLINFO message Windows Controls
topic_type:
- apiref
api_name:
- SBM_SETSCROLLINFO
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SBM\_SETSCROLLINFO message

The **SBM\_SETSCROLLINFO** message is sent to set the parameters of a scroll bar.

Applications should not send this message directly. Instead, they should use the [**SetScrollInfo**](/windows/desktop/api/Winuser/nf-winuser-setscrollinfo) function. A window receives this message through its [*WindowProc*](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function. Applications which implement a custom scroll bar control must respond to these messages for the **SetScrollInfo** function to function properly.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies whether the scroll bar is redrawn to reflect the new scroll box position. If this parameter is **TRUE**, the scroll bar is redrawn. If it is **FALSE**, the scroll bar is not redrawn.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**SCROLLINFO**](/windows/win32/api/winuser/ns-winuser-scrollinfo) structure. Before calling [**SetScrollInfo**](/windows/desktop/api/Winuser/nf-winuser-setscrollinfo), set the **cbSize** member of the structure to **sizeof**(**SCROLLINFO**), set the **fMask** member to indicate the parameters to set, and specify the new parameter values in the appropriate members.

The **fMask** member can be one or more of the following values.



| Value                                                                                                                                                                           | Meaning                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| <span id="SIF_DISABLENOSCROLL"></span><span id="sif_disablenoscroll"></span><dl> <dt>**SIF\_DISABLENOSCROLL**</dt> </dl> | Disables the scroll bar instead of removing it, if the scroll bar's new parameters make the scroll bar unnecessary.<br/> |
| <span id="SIF_PAGE"></span><span id="sif_page"></span><dl> <dt>**SIF\_PAGE**</dt> </dl>                                  | Sets the scroll page to the value specified in the **nPage** member.<br/>                                                |
| <span id="SIF_POS"></span><span id="sif_pos"></span><dl> <dt>**SIF\_POS**</dt> </dl>                                     | Sets the scroll position to the value specified in the **nPos** member. <br/>                                            |
| <span id="SIF_RANGE"></span><span id="sif_range"></span><dl> <dt>**SIF\_RANGE**</dt> </dl>                               | Sets the scroll range to the value specified in the **nMin** and **nMax** members. <br/>                                 |



 

</dd> </dl>

## Return value

The return value is the current position of the scroll box.

## Remarks

The messages that indicate scroll bar position, [**WM\_HSCROLL**](wm-hscroll.md) and [**WM\_VSCROLL**](wm-vscroll.md), provide only 16 bits of position data. However, the [**SCROLLINFO**](/windows/win32/api/winuser/ns-winuser-scrollinfo) structure used by [**SBM\_GETSCROLLINFO**](sbm-getscrollinfo.md), **SBM\_SETSCROLLINFO**, [**GetScrollInfo**](/windows/desktop/api/Winuser/nf-winuser-getscrollinfo), and [**SetScrollInfo**](/windows/desktop/api/Winuser/nf-winuser-setscrollinfo) provides 32 bits of scroll bar position data. You can use these messages and functions while processing either the **WM\_HSCROLL** or **WM\_VSCROLL** messages to obtain 32-bit scroll bar position data.

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

[**GetScrollInfo**](/windows/desktop/api/Winuser/nf-winuser-getscrollinfo)
</dt> <dt>

[**SBM\_GETSCROLLINFO**](sbm-getscrollinfo.md)
</dt> <dt>

[**SCROLLINFO**](/windows/win32/api/winuser/ns-winuser-scrollinfo)
</dt> <dt>

[**SetScrollInfo**](/windows/desktop/api/Winuser/nf-winuser-setscrollinfo)
</dt> </dl>

 

