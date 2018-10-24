---
title: BN_KILLFOCUS notification code
description: Sent when a button loses the keyboard focus. The button must have the BS\_NOTIFY style to send this notification code. The parent window of the button receives this notification code through the WM\_COMMAND message.
ms.assetid: 740154ba-47fd-4084-8b86-6166f1e1b39f
keywords:
- BN_KILLFOCUS notification code Windows Controls
topic_type:
- apiref
api_name:
- BN_KILLFOCUS
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BN\_KILLFOCUS notification code

Sent when a button loses the keyboard focus. The button must have the [**BS\_NOTIFY**](button-styles.md) style to send this notification code.

The parent window of the button receives this notification code through the [**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591) message.


```C++
BN_KILLFOCUS

    WPARAM wParam;
    LPARAM lParam; 
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) contains the button's control identifier. The [**HIWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632657) specifies the notification code.

</dd> <dt>

*lParam* 
</dt> <dd>

A handle to the button.

</dd> </dl>

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[BN\_SETFOCUS](bn-setfocus.md)
</dt> </dl>

 

 





