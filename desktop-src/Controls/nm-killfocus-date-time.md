---
title: NM_KILLFOCUS (date time) notification code (Commctrl.h)
description: Notifies a date and time picker control's parent window that the control has lost the input focus. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 33d6b88b-9608-4227-a822-1dc7a77d3a3f
keywords:
- NM_KILLFOCUS (date time) notification code Windows Controls
topic_type:
- apiref
api_name:
- NM_KILLFOCUS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# NM\_KILLFOCUS (date time) notification code

Notifies a date and time picker control's parent window that the control has lost the input focus. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_KILLFOCUS

    lpnmh = (LPNMHDR) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

The address of an [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) structure that contains additional information about this notification.

</dd> </dl>

## Return value

The return value is ignored.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





