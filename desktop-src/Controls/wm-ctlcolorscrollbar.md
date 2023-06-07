---
title: WM_CTLCOLORSCROLLBAR message (Winuser.h)
description: The WM\_CTLCOLORSCROLLBAR message is sent to the parent window of a scroll bar control when the control is about to be drawn.
ms.assetid: 35832a23-96f1-42cb-a986-06726bf2a124
keywords:
- WM_CTLCOLORSCROLLBAR message Windows Controls
topic_type:
- apiref
api_name:
- WM_CTLCOLORSCROLLBAR
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CTLCOLORSCROLLBAR message

The **WM\_CTLCOLORSCROLLBAR** message is sent to the parent window of a scroll bar control when the control is about to be drawn. By responding to this message, the parent window can use the display context handle to set the background color of the scroll bar control.

A window receives this message through its [*WindowProc*](/windows/win32/api/winuser/nc-winuser-wndproc) function.


```C++
WM_CTLCOLORSCROLLBAR

    WPARAM wParam
    LPARAM lParam; 
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Handle to the device context for the scroll bar control.

</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the scroll bar.

</dd> </dl>

## Return value

If an application processes this message, it must return the handle to a brush. The system uses the brush to paint the background of the scroll bar control.

## Remarks

If the application returns a brush that it created (for example, by using the [**CreateSolidBrush**](/windows/desktop/api/wingdi/nf-wingdi-createsolidbrush) or [**CreateBrushIndirect**](/windows/desktop/api/wingdi/nf-wingdi-createbrushindirect) function), the application must free the brush. If the application returns a system brush (for example, one that was retrieved by the [**GetStockObject**](/windows/desktop/api/wingdi/nf-wingdi-getstockobject) or [**GetSysColorBrush**](/windows/desktop/api/winuser/nf-winuser-getsyscolorbrush) function), the application does not need to free the brush.

By default, the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function selects the default system colors for the scroll bar control.

The **WM\_CTLCOLORSCROLLBAR** message is never sent between threads; it is only sent within the same thread.

If a dialog box procedure handles this message, it should cast the desired return value to a **INT\_PTR** and return the value directly. If the dialog box procedure returns **FALSE**, then default message handling is performed. The DWL\_MSGRESULT value set by the [**SetWindowLong**](/windows/desktop/api/winuser/nf-winuser-setwindowlonga) function is ignored.

The **WM\_CTLCOLORSCROLLBAR** message is used only by child scroll bar controls. Scrollbars attached to a window (WS\_SCROLL and WS\_VSCROLL) do not generate this message. To customize the appearance of scrollbars attached to a window, use the flat scroll bar functions.

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

[**WM\_CTLCOLORBTN**](wm-ctlcolorbtn.md)
</dt> <dt>

[**WM\_CTLCOLOREDIT**](wm-ctlcoloredit.md)
</dt> <dt>

[**WM\_CTLCOLORLISTBOX**](wm-ctlcolorlistbox.md)
</dt> <dt>

[**WM\_CTLCOLORSTATIC**](wm-ctlcolorstatic.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca)
</dt> <dt>

[**RealizePalette**](/windows/desktop/api/wingdi/nf-wingdi-realizepalette)
</dt> <dt>

[**SelectPalette**](/windows/desktop/api/wingdi/nf-wingdi-selectpalette)
</dt> <dt>

[**WM\_CTLCOLORDLG**](/windows/desktop/dlgbox/wm-ctlcolordlg)
</dt> </dl>

 

