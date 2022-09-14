---
title: ACN_STOP notification code (Commctrl.h)
description: Notifies the parent window of an animation control that the associated AVI clip has stopped playing. This notification code is sent in the form of a WM\_COMMAND message.
ms.assetid: 2f21a2ec-975f-4592-8b21-956bd5311ef4
keywords:
- ACN_STOP notification code Windows Controls
topic_type:
- apiref
api_name:
- ACN_STOP
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ACN\_STOP notification code

Notifies the parent window of an animation control that the associated AVI clip has stopped playing. This notification code is sent in the form of a [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message.


```C++
ACN_STOP     

    WPARAM wParam;
    LPARAM lParam;
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) contains the animation control's identifier. The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) specifies the notification code.

</dd> <dt>

*lParam* 
</dt> <dd>

An **HWND** that specifies the handle to the animation control.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

