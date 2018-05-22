---
title: NM\_DBLCLK (tab) notification code
description: Notifies a parent window of a tab control that the user has double-clicked the left mouse button within the control. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 'fd99f195-ceac-47e8-b584-d814b055fa21'
keywords: ["NM_DBLCLK (tab) notification code Windows Controls"]
topic_type:
- apiref
api_name:
- NM_DBLCLK
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# NM\_DBLCLK (tab) notification code

Notifies a parent window of a tab control that the user has double-clicked the left mouse button within the control. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_DBLCLK
        
    lpnmh = (LPNMHDR) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMHDR**](nmhdr.md) structure that contains additional information about this notification.

</dd> </dl>

## Return value

Return nonzero to not allow the default processing, or zero to allow the default processing.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





