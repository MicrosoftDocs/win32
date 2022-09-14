---
title: PGN_SCROLL notification code (Commctrl.h)
description: Notifies a pager control's parent window that the contained window is about to be scrolled. This notification is sent in the form of a WM\_NOTIFY message.
ms.assetid: 3d40e75e-c445-4885-b807-8cfcb92cb2d9
keywords:
- PGN_SCROLL notification code Windows Controls
topic_type:
- apiref
api_name:
- PGN_SCROLL
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PGN\_SCROLL notification code

Notifies a pager control's parent window that the contained window is about to be scrolled. This notification is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
PGN_SCROLL

    lpnms = (LPNMPGSCROLL) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMPGSCROLL**](/windows/desktop/api/Commctrl/ns-commctrl-nmpgscroll) structure that contains and receives information about the notification code. The **iDir** member of this structure indicates the direction of the scroll. The **iXpos** and **iYpos** members contain the horizontal and vertical position of the contained window prior to the scroll. The **iScroll** member contains the default scroll delta amount. You can modify this member to a different scroll amount if desired.

</dd> </dl>

## Return value

The return value is ignored.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





