---
title: NM_CHAR (toolbar) notification code (Commctrl.h)
description: Sent by a toolbar when it receives a WM\_CHAR message. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 7bf0b046-da8e-448f-94e1-62ba0989f7ba
keywords:
- NM_CHAR (toolbar) notification code Windows Controls
topic_type:
- apiref
api_name:
- NM_CHAR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# NM\_CHAR (toolbar) notification code

Sent by a toolbar when it receives a [**WM\_CHAR**](/windows/desktop/inputdev/wm-char) message. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
NM_CHAR

    lpnmc = (LPNMCHAR) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMCHAR**](/windows/win32/api/commctrl/ns-commctrl-nmchar) structure that contains additional information about the character that caused the notification code. The **dwItemPrev** member of this structure contains the command identifier of the item that is currently hot or -1 if no item is currently hot. The **dwItemNext** member of this structure contains the command identifier of the item that will become hot or -1 if the key does not match any item's accelerator.

</dd> </dl>

## Return value

Returns **TRUE** to indicate that the toolbar should not process the character and **FALSE** to have the toolbar process the character.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

