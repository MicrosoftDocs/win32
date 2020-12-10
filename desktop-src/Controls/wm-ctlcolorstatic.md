---
title: WM_CTLCOLORSTATIC message (Winuser.h)
description: A static control, or an edit control that is read-only or disabled, sends the WM\_CTLCOLORSTATIC message to its parent window when the control is about to be drawn.
ms.assetid: a171a1e8-6845-4a8e-8394-44cea99d2b0d
keywords:
- WM_CTLCOLORSTATIC message Windows Controls
topic_type:
- apiref
api_name:
- WM_CTLCOLORSTATIC
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CTLCOLORSTATIC message

A static control, or an edit control that is read-only or disabled, sends the **WM\_CTLCOLORSTATIC** message to its parent window when the control is about to be drawn. By responding to this message, the parent window can use the specified device context handle to set the text foreground and background colors of the static control.

A window receives this message through its [*WindowProc*](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.


```C++
WM_CTLCOLORSTATIC

    WPARAM wParam;
    LPARAM lParam; 
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Handle to the device context for the static control window.

</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the static control.

</dd> </dl>

## Return value

If an application processes this message, the return value is a handle to a brush that the system uses to paint the background of the static control.

## Remarks

If the application returns a brush that it created (for example, by using the [**CreateSolidBrush**](/windows/desktop/api/wingdi/nf-wingdi-createsolidbrush) or [**CreateBrushIndirect**](/windows/desktop/api/wingdi/nf-wingdi-createbrushindirect) function), the application must free the brush. If the application returns a system brush (for example, one that was retrieved by the [**GetStockObject**](/windows/desktop/api/wingdi/nf-wingdi-getstockobject) or [**GetSysColorBrush**](/windows/desktop/api/winuser/nf-winuser-getsyscolorbrush) function), the application does not need to free the brush.

By default, the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function selects the default system colors for the static control.

You can set the text background color of a disabled edit control, but you cannot set the text foreground color. The system always uses COLOR\_GRAYTEXT.

Edit controls that are not read-only or disabled do not send the **WM\_CTLCOLORSTATIC** message; instead, they send the [**WM\_CTLCOLOREDIT**](wm-ctlcoloredit.md) message.

The **WM\_CTLCOLORSTATIC** message is never sent between threads; it is sent only within the same thread.

If a dialog box procedure handles this message, it should cast the desired return value to a **INT\_PTR** and return the value directly. If the dialog box procedure returns **FALSE**, then default message handling is performed. The DWL\_MSGRESULT value set by the [**SetWindowLong**](/windows/desktop/api/winuser/nf-winuser-setwindowlonga) function is ignored.

## Examples

The following C++ example shows how to set the text foreground and background colors of a static control in response to the **WM\_CTLCOLORSTATIC** message. The `hbrBkgnd` variable is a static **HBRUSH** variable that is initialized to NULL, and stores the background brush between calls to **WM\_CTLCOLORSTATIC**. The brush must be destroyed by a call to the [**DeleteObject**](/windows/desktop/api/wingdi/nf-wingdi-deleteobject) function when it is no longer needed, typically when the associated dialog box is destroyed.


```C++
   case WM_CTLCOLORSTATIC:
        {
        HDC hdcStatic = (HDC) wParam;
        SetTextColor(hdcStatic, RGB(255,255,255));
        SetBkColor(hdcStatic, RGB(0,0,0));

        if (hbrBkgnd == NULL)
        {
            hbrBkgnd = CreateSolidBrush(RGB(0,0,0));
        }
        return (INT_PTR)hbrBkgnd;
        }
```



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

[**WM\_CTLCOLORSCROLLBAR**](wm-ctlcolorscrollbar.md)
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

 

