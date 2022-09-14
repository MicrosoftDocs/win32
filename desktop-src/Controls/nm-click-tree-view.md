---
title: NM_CLICK (tree view) notification code (Commctrl.h)
description: Notifies the parent window of a tree-view control that the user has clicked the left mouse button within the control. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 39b5716d-cae7-4dc4-b257-0118f4f432c6
keywords:
- NM_CLICK (tree view) notification code Windows Controls
topic_type:
- apiref
api_name:
- NM_CLICK
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# NM\_CLICK (tree view) notification code

Notifies the parent window of a tree-view control that the user has clicked the left mouse button within the control. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_CLICK
        
    lpnmh = (LPNMHDR) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) structure that contains additional information about this notification.

</dd> </dl>

## Return value

Return nonzero to prevent the default processing, or zero to allow the default processing.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





