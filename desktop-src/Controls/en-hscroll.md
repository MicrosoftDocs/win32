---
title: EN\_HSCROLL notification code
description: Sent when the user clicks an edit control's horizontal scroll bar. The parent window of the edit control receives this notification code through a WM\_COMMAND message. The parent window is notified before the screen is updated.
ms.assetid: 'beaaa80c-4108-4a8e-aed8-04c9a3a08f3e'
keywords: ["EN_HSCROLL notification code Windows Controls"]
topic_type:
- apiref
api_name:
- EN_HSCROLL
api_location:
- Winuser.h
api_type:
- HeaderDef
---

# EN\_HSCROLL notification code

Sent when the user clicks an edit control's horizontal scroll bar. The parent window of the edit control receives this notification code through a [**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591) message. The parent window is notified before the screen is updated.


```C++
EN_HSCROLL

    WPARAM wParam;
    LPARAM lParam;
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) contains the identifier of the edit control. The [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) specifies the notification code.

</dd> <dt>

*lParam* 
</dt> <dd>

A handle to the edit control.

</dd> </dl>

## Remarks

This notification code is sent for the following mouse events on the horizontal scroll bar: clicking either arrow button or clicking between the arrow button and the thumb. However, the notification code is not sent when clicking the scroll bar thumb itself. The notification code is also sent when a keyboard event causes a change in the view area of the edit control, for example, pressing HOME, END, LEFT ARROW, or RIGHT ARROW.

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. To receive **EN\_HSCROLL** notification codes, specify [**ENM\_SCROLL**](rich-edit-control-event-mask-flags.md#enm-scroll) in the mask sent with the [**EM\_SETEVENTMASK**](em-seteventmask.md) message. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[EN\_VSCROLL](en-vscroll.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591)
</dt> </dl>

 

 





