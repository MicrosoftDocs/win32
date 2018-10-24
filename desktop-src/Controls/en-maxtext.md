---
title: EN_MAXTEXT notification code
description: Sent when the current text insertion has exceeded the specified number of characters for the edit control.
ms.assetid: b03835d6-d06f-415a-97f2-d2b62b17e175
keywords:
- EN_MAXTEXT notification code Windows Controls
topic_type:
- apiref
api_name:
- EN_MAXTEXT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EN\_MAXTEXT notification code

Sent when the current text insertion has exceeded the specified number of characters for the edit control. The text insertion has been truncated.

This notification code is also sent when an edit control does not have the [**ES\_AUTOHSCROLL**](edit-control-styles.md) style and the number of characters to be inserted would exceed the width of the edit control.

This notification code is also sent when an edit control does not have the [**ES\_AUTOVSCROLL**](edit-control-styles.md) style and the total number of lines resulting from a text insertion would exceed the height of the edit control.

The parent window of the edit control receives this notification code through a [**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591) message.


```C++
EN_MAXTEXT

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

The parent window always receives a [**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591) message for this event, it does not require a notification mask sent with [**EM\_SETEVENTMASK**](em-seteventmask.md).

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591)
</dt> </dl>

 

 





