---
title: LVN_GETINFOTIP notification code (Commctrl.h)
description: Sent by a large icon view list-view control that has the LVS\_EX\_INFOTIP extended style.
ms.assetid: 62be5087-7e49-4722-a63a-1768e030af48
keywords:
- LVN_GETINFOTIP notification code Windows Controls
topic_type:
- apiref
api_name:
- LVN_GETINFOTIP
- LVN_GETINFOTIPA
- LVN_GETINFOTIPW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVN\_GETINFOTIP notification code

Sent by a large icon view list-view control that has the [**LVS\_EX\_INFOTIP**](extended-list-view-styles.md) extended style. This notification code is sent when the list-view control is requesting additional text information to be displayed in a tooltip. It is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
LVN_GETINFOTIP

    pGetInfoTip = (LPNMLVGETINFOTIP) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMLVGETINFOTIP**](/windows/win32/api/commctrl/ns-commctrl-nmlvgetinfotipa) structure that contains information about this notification code.

</dd> </dl>

## Return value

The return value for this notification is not used.

## Remarks

This notification code is only sent by list-view controls that have the [**LVS\_EX\_INFOTIP**](extended-list-view-styles.md) extended style. The LVN\_GETINFOTIP notification code is sent only for subitem 0.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **LVN\_GETINFOTIPW** (Unicode) and **LVN\_GETINFOTIPA** (ANSI)<br/>             |



 

 





