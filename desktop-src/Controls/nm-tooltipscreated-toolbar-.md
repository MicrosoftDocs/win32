---
title: NM_TOOLTIPSCREATED (toolbar) notification code (Commctrl.h)
description: Notifies a toolbar's parent window that the toolbar has created a tooltip control. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 0e9517c1-aa3f-4b14-82b4-195a4ce99757
keywords:
- NM_TOOLTIPSCREATED (toolbar) notification code Windows Controls
topic_type:
- apiref
api_name:
- NM_TOOLTIPSCREATED
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# NM\_TOOLTIPSCREATED (toolbar) notification code

Notifies a toolbar's parent window that the toolbar has created a tooltip control. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_TOOLTIPSCREATED

    lpnmttc = (LPNMTOOLTIPSCREATED) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTOOLTIPSCREATED**](/windows/win32/api/commctrl/ns-commctrl-nmtooltipscreated) structure that contains additional information about this notification.

</dd> </dl>

## Return value

The toolbar control ignores the return value from this notification code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





