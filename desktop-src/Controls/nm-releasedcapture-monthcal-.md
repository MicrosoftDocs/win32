---
title: NM_RELEASEDCAPTURE (monthcal) notification code (Commctrl.h)
description: Notifies a monthcal control's parent window that the control is releasing mouse capture. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: c05d3331-26f3-41f4-8032-36ed38d47917
keywords:
- NM_RELEASEDCAPTURE (monthcal) notification code Windows Controls
topic_type:
- apiref
api_name:
- NM_RELEASEDCAPTURE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# NM\_RELEASEDCAPTURE (monthcal) notification code

Notifies a monthcal control's parent window that the control is releasing mouse capture. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_RELEASEDCAPTURE

    lpnmh = (LPNMHDR) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) structure that contains additional information about this notification.

</dd> </dl>

## Return value

The control ignores the return value from this notification code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





