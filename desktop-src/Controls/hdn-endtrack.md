---
title: HDN_ENDTRACK notification code (Commctrl.h)
description: Notifies a header control's parent window that the user has finished dragging a divider. This notification code sent in the form of a WM\_NOTIFY message.
ms.assetid: d9b25871-7bd6-439c-91b8-e8249d9be67d
keywords:
- HDN_ENDTRACK notification code Windows Controls
topic_type:
- apiref
api_name:
- HDN_ENDTRACK
- HDN_ENDTRACKA
- HDN_ENDTRACKW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# HDN\_ENDTRACK notification code

Notifies a header control's parent window that the user has finished dragging a divider. This notification code sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
HDN_ENDTRACK

    pNMHeader = (LPNMHEADER) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMHEADER**](/windows/win32/api/commctrl/ns-commctrl-nmheadera) structure that contains information about the header control and the item whose divider was dragged.

</dd> </dl>

## Return value

No return value.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **HDN\_ENDTRACKW** (Unicode) and **HDN\_ENDTRACKA** (ANSI)<br/>                 |



 

 





