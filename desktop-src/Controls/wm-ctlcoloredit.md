---
title: WM_CTLCOLOREDIT message (Winuser.h)
description: An edit control that is not read-only or disabled sends the WM\_CTLCOLOREDIT message to its parent window when the control is about to be drawn.
ms.assetid: 2294e3b8-00a7-43ef-b20a-fe0e46764055
keywords:
- WM_CTLCOLOREDIT message Windows Controls
topic_type:
- apiref
api_name:
- WM_CTLCOLOREDIT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CTLCOLOREDIT message

An edit control that is not read-only or disabled sends the **WM\_CTLCOLOREDIT** message to its parent window when the control is about to be drawn. By responding to this message, the parent window can use the specified device context handle to set the text and background colors of the edit control.


```C++
WM_CTLCOLOREDIT

    WPARAM wParam;
    LPARAM lParam; 
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the device context for the edit control window.

</dd> <dt>

*lParam* 
</dt> <dd>

A handle to the edit control.

</dd> </dl>

## Return value

If an application processes this message, it must return the handle of a brush. The system uses the brush to paint the background of the edit control.

## Remarks

If the application returns a brush that it created (for example, by using the [**CreateSolidBrush**](/windows/desktop/api/wingdi/nf-wingdi-createsolidbrush) or [**CreateBrushIndirect**](/windows/desktop/api/wingdi/nf-wingdi-createbrushindirect) function), the application must free the brush. If the application returns a system brush (for example, one that was retrieved by the [**GetStockObject**](/windows/desktop/api/wingdi/nf-wingdi-getstockobject) or [**GetSysColorBrush**](/windows/desktop/api/winuser/nf-winuser-getsyscolorbrush) function), the application does not need to free the brush.

By default, the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function selects the default system colors for the edit control.

Read-only or disabled edit controls do not send the **WM\_CTLCOLOREDIT** message; instead, they send the [**WM\_CTLCOLORSTATIC**](wm-ctlcolorstatic.md) message.

The **WM\_CTLCOLOREDIT** message is never sent between threads, it is only sent within the same thread.

If a dialog box procedure handles this message, it should cast the desired return value to a **INT\_PTR** and return the value directly. If the dialog box procedure returns **FALSE**, then default message handling is performed. The DWL\_MSGRESULT value set by the [**SetWindowLong**](/windows/desktop/api/winuser/nf-winuser-setwindowlonga) function is ignored.

**Rich Edit:** This message is not supported. To set the background color for a rich edit control, use the [**EM\_SETBKGNDCOLOR**](em-setbkgndcolor.md) message.

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

[**EM\_SETBKGNDCOLOR**](em-setbkgndcolor.md)
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
</dt> </dl>

 

