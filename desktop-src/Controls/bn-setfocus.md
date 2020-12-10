---
title: BN_SETFOCUS notification code (Winuser.h)
description: Sent when a button receives the keyboard focus. The button must have the BS\_NOTIFY style to send this notification code. The parent window of the button receives this notification code through the WM\_COMMAND message.
ms.assetid: 6b8d9bde-67f9-454f-ba2c-e5c8d9ff2709
keywords:
- BN_SETFOCUS notification code Windows Controls
topic_type:
- apiref
api_name:
- BN_SETFOCUS
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# BN\_SETFOCUS notification code

Sent when a button receives the keyboard focus. The button must have the [**BS\_NOTIFY**](button-styles.md) style to send this notification code.

The parent window of the button receives this notification code through the [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message.


```C++
BN_SETFOCUS

    WPARAM wParam;
    LPARAM lParam; 
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) contains the button's control identifier. The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) specifies the notification code.

</dd> <dt>

*lParam* 
</dt> <dd>

A handle to the button.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[BN\_KILLFOCUS](bn-killfocus.md)
</dt> </dl>

 

