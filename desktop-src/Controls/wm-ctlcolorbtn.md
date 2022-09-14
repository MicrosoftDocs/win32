---
title: WM_CTLCOLORBTN message (Winuser.h)
description: The WM\_CTLCOLORBTN message is sent to the parent window of a button before drawing the button. The parent window can change the button's text and background colors. However, only owner-drawn buttons respond to the parent window processing this message.
ms.assetid: fd2ab917-ffd6-4f71-9b1c-0ecdfe53ae8b
keywords:
- WM_CTLCOLORBTN message Windows Controls
topic_type:
- apiref
api_name:
- WM_CTLCOLORBTN
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CTLCOLORBTN message

The **WM\_CTLCOLORBTN** message is sent to the parent window of a button before drawing the button. The parent window can change the button's text and background colors. However, only owner-drawn buttons respond to the parent window processing this message.


```C++
WM_CTLCOLORBTN

    WPARAM wParam;
    LPARAM lParam; 
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

An **HDC** that specifies the handle to the display context for the button.

</dd> <dt>

*lParam* 
</dt> <dd>

An **HWND** that specifies the handle to the button.

</dd> </dl>

## Return value

If an application processes this message, it must return a handle to a brush. The system uses the brush to paint the background of the button.

## Remarks

If the application returns a brush that it created (for example, by using the [**CreateSolidBrush**](/windows/desktop/api/wingdi/nf-wingdi-createsolidbrush) or [**CreateBrushIndirect**](/windows/desktop/api/wingdi/nf-wingdi-createbrushindirect) function), the application must free the brush. If the application returns a system brush (for example, one that was retrieved by the [**GetStockObject**](/windows/desktop/api/wingdi/nf-wingdi-getstockobject) or [**GetSysColorBrush**](/windows/desktop/api/winuser/nf-winuser-getsyscolorbrush) function), the application does not need to free the brush.

By default, the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function selects the default system colors for the button. Buttons with the [**BS\_PUSHBUTTON**](button-styles.md), [**BS\_DEFPUSHBUTTON**](button-styles.md), or [**BS\_PUSHLIKE**](button-styles.md) styles do not use the returned brush. Buttons with these styles are always drawn with the default system colors. Drawing push buttons requires several different brushes-face, highlight, and shadow-but the **WM\_CTLCOLORBTN** message allows only one brush to be returned. To provide a custom appearance for push buttons, use an owner-drawn button. For more information, see [Creating Owner-Drawn Controls](user-controls-intro.md).

The **WM\_CTLCOLORBTN** message is never sent between threads. It is sent only within one thread.

The text color of a check box or radio button applies to the box or button, its check mark, and the text. The focus rectangle for these buttons remains the system default color (typically black). The text color of a group box applies to the text but not to the line that defines the box. The text color of a push button applies only to its focus rectangle; it does not affect the color of the text.

If a dialog box procedure handles this message, it should cast the desired return value to a **INT\_PTR** and return the value directly. If the dialog box procedure returns **FALSE**, then default message handling is performed. The DWL\_MSGRESULT value set by the [**SetWindowLong**](/windows/desktop/api/winuser/nf-winuser-setwindowlonga) function is ignored.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Other Resources**
</dt> <dt>

[**RealizePalette**](/windows/desktop/api/wingdi/nf-wingdi-realizepalette)
</dt> <dt>

[**SelectPalette**](/windows/desktop/api/wingdi/nf-wingdi-selectpalette)
</dt> </dl>

 

