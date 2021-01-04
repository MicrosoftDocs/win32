---
title: BN_PUSHED notification code (Winuser.h)
description: Sent when the push state of a button is set to pushed.
ms.assetid: 34000def-189c-4a37-bcef-4ca09a67df00
keywords:
- BN_PUSHED notification code Windows Controls
topic_type:
- apiref
api_name:
- BN_PUSHED
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# BN\_PUSHED notification code

Sent when the push state of a button is set to pushed.

> [!Note]  
> This notification code is provided only for compatibility with 16-bit versions of Windows earlier than version 3.0. Applications should use the [**BS\_OWNERDRAW**](button-styles.md) button style and the [**DRAWITEMSTRUCT**](/windows/win32/api/winuser/ns-winuser-drawitemstruct) structure for this task.

 

The parent window of the button receives this notification code through the [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message.


```C++
BN_PUSHED

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

## Remarks

BN\_PUSHED is the same as the [BN\_HILITE](bn-hilite.md) notification code.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**BN\_UNPUSHED**](bn-unpushed.md)
</dt> </dl>

 

