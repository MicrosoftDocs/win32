---
title: TVN_GETDISPINFO notification code (Commctrl.h)
description: Requests that a tree-view control's parent window provide information needed to display or sort an item. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 2dfe41d8-1164-481b-ac07-8faba43c562a
keywords:
- TVN_GETDISPINFO notification code Windows Controls
topic_type:
- apiref
api_name:
- TVN_GETDISPINFO
- TVN_GETDISPINFOA
- TVN_GETDISPINFOW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVN\_GETDISPINFO notification code

Requests that a tree-view control's parent window provide information needed to display or sort an item. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TVN_GETDISPINFO 

    lptvdi = (LPNMTVDISPINFO) lParam 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTVDISPINFO**](/windows/win32/api/commctrl/ns-commctrl-nmtvdispinfoa) structure. The **item** member is a [**TVITEM**](/windows/win32/api/commctrl/ns-commctrl-tvitema) structure whose **mask**, **hItem**, **state**, and **lParam** members specify the type of information required. You must fill the members of the structure with the appropriate information.

</dd> </dl>

## Return value

The return value is ignored.

## Remarks

This notification code is sent under the following circumstances:

-   If the **pszText** member of the item's [**TVITEM**](/windows/win32/api/commctrl/ns-commctrl-tvitema) structure is the LPSTR\_TEXTCALLBACK value, the control sends this notification code to retrieve the item's text. In this case, the **mask** member of *lParam* will have the TVIF\_TEXT flag set.
-   If the **iImage** or **iSelectedImage** member of the item's [**TVITEM**](/windows/win32/api/commctrl/ns-commctrl-tvitema) structure is the I\_IMAGECALLBACK value, the control sends this notification code to retrieve the index of an item's icons in the control's image list. In this case, if the item is selected, the **mask** member of *lParam* will have the TVIF\_SELECTEDIMAGE flag set. If the item is not selected, the **mask** member of *lParam* will have the TVIF\_IMAGE flag set.
-   If the **cChildren** member of the item's [**TVITEM**](/windows/win32/api/commctrl/ns-commctrl-tvitema) structure is the I\_CHILDRENCALLBACK value, the control sends this notification code to retrieve a value that indicates whether the item has child items. In this case, the **mask** member of *lParam* will have the TVIF\_CHILDREN flag set.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TVN\_GETDISPINFOW** (Unicode) and **TVN\_GETDISPINFOA** (ANSI)<br/>           |



## See also

<dl> <dt>

[TVN\_SETDISPINFO](tvn-setdispinfo.md)
</dt> </dl>

 

 





