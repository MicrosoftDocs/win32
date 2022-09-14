---
title: TBN_GETDISPINFO notification code (Commctrl.h)
description: Retrieves display information for a toolbar item. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: ed6e4141-2bf8-4a92-8349-f3833c87fcf3
keywords:
- TBN_GETDISPINFO notification code Windows Controls
ms.topic: reference
ms.date: 05/31/2018
---

# TBN\_GETDISPINFO notification code

Retrieves display information for a toolbar item. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TBN_GETDISPINFO 

    lptbdi = (LPNMTBDISPINFO) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTBDISPINFO**](/windows/desktop/api/Commctrl/ns-commctrl-nmtbdispinfoa) structure. The **idCommand** member specifies the item's command identifier, the **lParam** member contains the item's application-defined data, and the **dwMask** member specifies what information is being requested.

</dd> </dl>

## Return value

The return value is ignored by the control.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TBN\_GETDISPINFOW** (Unicode) and **TBN\_GETDISPINFOA** (ANSI)<br/>           |



 

 





