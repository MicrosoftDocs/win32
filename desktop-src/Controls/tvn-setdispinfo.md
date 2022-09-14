---
title: TVN_SETDISPINFO notification code (Commctrl.h)
description: Notifies a tree-view control's parent window that it must update the information it maintains about an item. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 40fa61bc-c043-4001-ada9-b627d68bd737
keywords:
- TVN_SETDISPINFO notification code Windows Controls
topic_type:
- apiref
api_name:
- TVN_SETDISPINFO
- TVN_SETDISPINFOA
- TVN_SETDISPINFOW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVN\_SETDISPINFO notification code

Notifies a tree-view control's parent window that it must update the information it maintains about an item. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TVN_SETDISPINFO 

    lptvdi = (LPNMTVDISPINFO) lParam 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTVDISPINFO**](/windows/win32/api/commctrl/ns-commctrl-nmtvdispinfoa) structure that describes the item being updated. The **hItem** member of the [**TVITEM**](/windows/win32/api/commctrl/ns-commctrl-tvitema) structure specifies the item being updated, and the **mask** member specifies which attributes of the item are being updated.

</dd> </dl>

## Return value

The return value is ignored.

## Remarks

If the **pszText** member of the item's [**TVITEM**](/windows/win32/api/commctrl/ns-commctrl-tvitema) structure is the LPSTR\_TEXTCALLBACK value, the control sends this notification to set the item's text. In this case, the **mask** member of *lParam* will have the TVIF\_TEXT flag set.

If the **iImage** or **iSelectedImage** member of the item's [**TVITEM**](/windows/win32/api/commctrl/ns-commctrl-tvitema) structure is the I\_IMAGECALLBACK value, the control sends this notification to retrieve the index of the icon image to display. In this case, the **mask** member of *lParam* will have the TVIF\_IMAGE or TVIF\_SELECTEDIMAGE flag set.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TVN\_SETDISPINFOW** (Unicode) and **TVN\_SETDISPINFOA** (ANSI)<br/>           |



## See also

<dl> <dt>

[**TVITEM**](/windows/win32/api/commctrl/ns-commctrl-tvitema)
</dt> <dt>

[**TVITEMEX**](/windows/win32/api/commctrl/ns-commctrl-tvitemexa)
</dt> <dt>

[TVN\_GETDISPINFO](tvn-getdispinfo.md)
</dt> </dl>

 

 





