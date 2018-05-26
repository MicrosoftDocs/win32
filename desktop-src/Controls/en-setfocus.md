---
title: EN\_SETFOCUS notification code
description: Sent when an edit control receives the keyboard focus. The parent window of the edit control receives this notification code through a WM\_COMMAND message.
ms.assetid: 482d2afa-4e21-4f3f-bdf4-6966b34cc3c4
keywords:
- EN_SETFOCUS notification code Windows Controls
topic_type:
- apiref
api_name:
- EN_SETFOCUS
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EN\_SETFOCUS notification code

Sent when an edit control receives the keyboard focus. The parent window of the edit control receives this notification code through a [**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591) message.


```C++
EN_SETFOCUS

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

**Reference**
</dt> <dt>

[EN\_KILLFOCUS](en-killfocus.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591)
</dt> </dl>

 

 





