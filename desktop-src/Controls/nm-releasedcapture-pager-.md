---
title: NM_RELEASEDCAPTURE (pager) notification code (Commctrl.h)
description: Notifies a pager control's parent window that the control has released the mouse capture. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 5ce9c38a-5d37-4ac7-8510-30bc59d85cca
keywords:
- NM_RELEASEDCAPTURE (pager) notification code Windows Controls
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

# NM\_RELEASEDCAPTURE (pager) notification code

Notifies a pager control's parent window that the control has released the mouse capture. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


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

The return value is ignored by the pager control.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





