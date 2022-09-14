---
title: TVN_DELETEITEM notification code (Commctrl.h)
description: Notifies a tree-view control's parent window that an item is being deleted. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 0d8801e0-02ae-40c9-8625-83d98b434d0a
keywords:
- TVN_DELETEITEM notification code Windows Controls
topic_type:
- apiref
api_name:
- TVN_DELETEITEM
- TVN_DELETEITEMA
- TVN_DELETEITEMW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVN\_DELETEITEM notification code

Notifies a tree-view control's parent window that an item is being deleted. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TVN_DELETEITEM 

    pnmtv = (LPNMTREEVIEW) lParam 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTREEVIEW**](/windows/win32/api/commctrl/ns-commctrl-nmtreeviewa) structure. The **itemOld** member is a [**TVITEM**](/windows/win32/api/commctrl/ns-commctrl-tvitema) structure whose **hItem** and **lParam** members contain valid information about the item being deleted.

</dd> </dl>

## Return value

The return value is ignored.

## Remarks

If the **lParam** member of the [**TVITEM**](/windows/win32/api/commctrl/ns-commctrl-tvitema) structure points to memory allocated by your application, you can free it when you receive the TVN\_DELETEITEM notification code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TVN\_DELETEITEMW** (Unicode) and **TVN\_DELETEITEMA** (ANSI)<br/>             |



 

 





