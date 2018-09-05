---
title: HDN_GETDISPINFO notification code
description: Sent to the owner of a header control when the control needs information about a callback header item. This notification code is sent as a WM\_NOTIFY message.
ms.assetid: 51522df0-83ae-4d9a-a8fc-31083e24242a
keywords:
- HDN_GETDISPINFO notification code Windows Controls
topic_type:
- apiref
api_name:
- HDN_GETDISPINFO
- HDN_GETDISPINFOA
- HDN_GETDISPINFOW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HDN\_GETDISPINFO notification code

Sent to the owner of a header control when the control needs information about a callback header item. This notification code is sent as a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
HDN_GETDISPINFO

   pNMHDDispInfo = (LPNMHDDISPINFO) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMHDDISPINFO**](/windows/desktop/api/Commctrl/ns-commctrl-tagnmhddispinfoa) structure. On input, the fields of the structure specify what information is required and the item of interest.

</dd> </dl>

## Return value

Returns an LRESULT.

## Remarks

Fill the appropriate members of the structure to return the requested information to the header control. If your message handler sets the **mask** member of the [**NMHDDISPINFO**](/windows/desktop/api/Commctrl/ns-commctrl-tagnmhddispinfoa) structure to HDI\_DI\_SETITEM, the header control stores the information and will not request it again.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **HDN\_GETDISPINFOW** (Unicode) and **HDN\_GETDISPINFOA** (ANSI)<br/>           |



 

 





