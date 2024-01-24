---
title: LVN_MARQUEEBEGIN notification code (Commctrl.h)
description: Notifies a list-view control's parent window that a bounding box (marquee) selection has begun. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: e9daa264-1861-4791-9a12-cf95d86a688e
keywords:
- LVN_MARQUEEBEGIN notification code Windows Controls
topic_type:
- apiref
api_name:
- LVN_MARQUEEBEGIN
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVN\_MARQUEEBEGIN notification code

Notifies a list-view control's parent window that a bounding box (marquee) selection has begun. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
LVN_MARQUEEBEGIN

    pnmv = (LPNMLISTVIEW) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) structure.

</dd> </dl>

## Return value

To accept the notification code, return zero. To quit the bounding box selection, return nonzero.

## Remarks

A *bounding box selection* is the process of clicking the list-view window's client area and dragging to select multiple items simultaneously.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





