---
title: TVN_ITEMCHANGED notification code (Commctrl.h)
description: Notifies a tree-view control's parent window that item attributes have changed. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: b09164bc-54da-457a-9fb7-3beab3dae3e4
keywords:
- TVN_ITEMCHANGED notification code Windows Controls
topic_type:
- apiref
api_name:
- TVN_ITEMCHANGED
- TVN_ITEMCHANGEDA
- TVN_ITEMCHANGEDW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVN\_ITEMCHANGED notification code

Notifies a tree-view control's parent window that item attributes have changed. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TVN_ITEMCHANGED
        
    pnm = (NMTVITEMCHANGE *) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**NMTVITEMCHANGE**](/windows/win32/api/commctrl/ns-commctrl-nmtvitemchange) structure describing the item that changed. The **uChanged** member is set to TVIF\_STATE.

</dd> </dl>

## Return value

Returns **FALSE** to accept the change, or **TRUE** to prevent the change.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TVN\_ITEMCHANGEDW** (Unicode) and **TVN\_ITEMCHANGEDA** (ANSI)<br/>           |



## See also

<dl> <dt>

[TVN\_ITEMCHANGING](tvn-itemchanging.md)
</dt> </dl>

 

 





