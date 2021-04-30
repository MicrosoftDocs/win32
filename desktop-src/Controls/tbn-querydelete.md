---
title: TBN_QUERYDELETE notification code (Commctrl.h)
description: Notifies the toolbar's parent window whether a button may be deleted from a toolbar while the user is customizing the toolbar. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: fa6a8fe4-a9a3-4c59-9237-d28bd34d664c
keywords:
- TBN_QUERYDELETE notification code Windows Controls
topic_type:
- apiref
api_name:
- TBN_QUERYDELETE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBN\_QUERYDELETE notification code

Notifies the toolbar's parent window whether a button may be deleted from a toolbar while the user is customizing the toolbar. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TBN_QUERYDELETE 

    lpnmtb = (LPNMTOOLBAR) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTOOLBAR**](/windows/win32/api/commctrl/ns-commctrl-nmtoolbara) structure. The **iItem** member contains the zero-based index of the button to be deleted.

</dd> </dl>

## Return value

Returns **TRUE** to allow the button to be deleted, or **FALSE** to prevent the button from being deleted.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





