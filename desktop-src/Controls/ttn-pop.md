---
title: TTN_POP notification code (Commctrl.h)
description: Notifies the owner window that a tooltip is about to be hidden. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 44a38f1a-f1df-4057-bf76-f87eb467f0d7
keywords:
- TTN_POP notification code Windows Controls
topic_type:
- apiref
api_name:
- TTN_POP
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TTN\_POP notification code

Notifies the owner window that a tooltip is about to be hidden. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TTN_POP

    pnmh = (LPNMHDR) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) structure.

</dd> </dl>

## Return value

No return value.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





