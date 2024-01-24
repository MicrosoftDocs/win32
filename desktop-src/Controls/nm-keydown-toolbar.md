---
title: NM_KEYDOWN (toolbar) notification code (Commctrl.h)
description: NM_KEYDOWN (toolbar) notification code - Sent by a control when the control has the keyboard focus and the user presses a key. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: bdfcf9da-118b-4fe6-9a0a-6329eb9196ef
keywords:
- NM_KEYDOWN (toolbar) notification code Windows Controls
topic_type:
- apiref
api_name:
- NM_KEYDOWN
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# NM\_KEYDOWN (toolbar) notification code

Sent by a control when the control has the keyboard focus and the user presses a key. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_KEYDOWN

    lpnmk = (LPNMKEY) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMKEY**](/windows/win32/api/commctrl/ns-commctrl-nmkey) structure that contains additional information about the key that caused the notification code.

</dd> </dl>

## Return value

Return nonzero to prevent the control from processing the key, or zero otherwise.

## Remarks

Currently, only the toolbar control sends this notification code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





