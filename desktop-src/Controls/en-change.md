---
title: EN_CHANGE notification code (Winuser.h)
description: Sent when the user has taken an action that may have altered text in an edit control.
ms.assetid: 8a04e6fb-ae9d-4d94-8047-6de96df899f5
keywords:
- EN_CHANGE notification code Windows Controls
topic_type:
- apiref
api_name:
- EN_CHANGE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EN\_CHANGE notification code

Sent when the user has taken an action that may have altered text in an edit control. Unlike the [EN\_UPDATE](en-update.md) notification code, this notification code is sent after the system updates the screen. The parent window of the edit control receives this notification code through a [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message.


```C++
EN_CHANGE

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

**Rich Edit:** Supported in Microsoft Rich Edit 1.0 and later. To receive EN\_CHANGE notification codes, specify [**ENM\_CHANGE**](rich-edit-control-event-mask-flags.md) in the mask sent with the [**EM\_SETEVENTMASK**](em-seteventmask.md) message. For information about the compatibility of rich edit versions with the various system versions, see [About Rich Edit Controls](about-rich-edit-controls.md).

The EN\_CHANGE notification code is not sent when the [**ES\_MULTILINE**](edit-control-styles.md) style is used and the text is sent through [**WM\_SETTEXT**](/windows/desktop/winmsg/wm-settext).

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

[EN\_UPDATE](en-update.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**WM\_COMMAND**](/windows/desktop/menurc/wm-command)
</dt> </dl>

 

