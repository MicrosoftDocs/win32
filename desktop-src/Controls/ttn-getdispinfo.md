---
title: TTN_GETDISPINFO notification code (Commctrl.h)
description: Sent by a tooltip control to retrieve information needed to display a tooltip window. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: af9ecc27-2004-4c45-9f1d-9ee0b2b50ff6
keywords:
- TTN_GETDISPINFO notification code Windows Controls
topic_type:
- apiref
api_name:
- TTN_GETDISPINFO
- TTN_GETDISPINFOA
- TTN_GETDISPINFOW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TTN\_GETDISPINFO notification code

Sent by a tooltip control to retrieve information needed to display a tooltip window. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TTN_GETDISPINFO

    lpnmtdi = (LPNMTTDISPINFO) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTTDISPINFO**](/windows/win32/api/commctrl/ns-commctrl-nmttdispinfoa) structure that identifies the tool that needs text and receives the requested information.

</dd> </dl>

## Return value

The return value for this notification is not used.

## Remarks

Fill the structure's appropriate members to return the requested information to the tooltip control. If your message handler sets the **uFlags** member of the [**NMTTDISPINFO**](/windows/win32/api/commctrl/ns-commctrl-nmttdispinfoa) structure to TTF\_DI\_SETITEM, the tooltip control stores the information and will not request it again.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TTN\_GETDISPINFOW** (Unicode) and **TTN\_GETDISPINFOA** (ANSI)<br/>           |



 

 





