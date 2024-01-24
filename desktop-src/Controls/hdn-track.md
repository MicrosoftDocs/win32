---
title: HDN_TRACK notification code (Commctrl.h)
description: Notifies a header control's parent window that the user is dragging a divider in the header control. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 26660ae1-0d6e-4ee7-8b6a-d621abef352d
keywords:
- HDN_TRACK notification code Windows Controls
topic_type:
- apiref
api_name:
- HDN_TRACK
- HDN_TRACKA
- HDN_TRACKW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# HDN\_TRACK notification code

Notifies a header control's parent window that the user is dragging a divider in the header control. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
HDN_TRACK

    pNMHeader = (LPNMHEADER) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMHEADER**](/windows/win32/api/commctrl/ns-commctrl-nmheadera) structure that contains information about the header control and the item whose divider is being dragged.

</dd> </dl>

## Return value

Returns **FALSE** to continue tracking the divider, or **TRUE** to end tracking.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **HDN\_TRACKW** (Unicode) and **HDN\_TRACKA** (ANSI)<br/>                       |



 

 





