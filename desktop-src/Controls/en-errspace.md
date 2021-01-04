---
title: EN_ERRSPACE notification code (Winuser.h)
description: Sent when an edit control cannot allocate enough memory to meet a specific request. The parent window of the edit control receives this notification code through a WM\_COMMAND message.
ms.assetid: 23a6eb10-a9d7-4fd5-9176-407c35e6f492
keywords:
- EN_ERRSPACE notification code Windows Controls
topic_type:
- apiref
api_name:
- EN_ERRSPACE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EN\_ERRSPACE notification code

Sent when an edit control cannot allocate enough memory to meet a specific request. The parent window of the edit control receives this notification code through a [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message.


```C++
EN_ERRSPACE

    WPARAM wParam;
    LPARAM lParam;
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) contains the identifier of the edit control. The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) specifies the notification code.

</dd> <dt>

*lParam* 
</dt> <dd>

A handle to the edit control.

</dd> </dl>

## Remarks

The parent window will always get a [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message for this event; it does not require a notification mask sent with the [**EM\_SETEVENTMASK**](em-seteventmask.md) message.

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**WM\_COMMAND**](/windows/desktop/menurc/wm-command)
</dt> </dl>

 

