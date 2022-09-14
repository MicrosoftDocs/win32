---
title: ACN_START notification code (Commctrl.h)
description: Notifies an animation control's parent window that the associated AVI clip has started playing. This notification code is sent in the form of a WM\_COMMAND message.
ms.assetid: b4d12225-36f7-4f87-b58a-dac091d14e4c
keywords:
- ACN_START notification code Windows Controls
topic_type:
- apiref
api_name:
- ACN_START
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ACN\_START notification code

Notifies an animation control's parent window that the associated AVI clip has started playing. This notification code is sent in the form of a [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message.


```C++
ACN_START 

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



 

