---
title: MCN_GETDAYSTATE notification code (Commctrl.h)
description: Sent by a month calendar control to request information about how individual days should be displayed. This notification code is sent only by month calendar controls that use the MCS\_DAYSTATE style, and it is sent in the form of a WM\_NOTIFY message.
ms.assetid: dc2608e0-c598-4b26-9195-208f09cd84b7
keywords:
- MCN_GETDAYSTATE notification code Windows Controls
topic_type:
- apiref
api_name:
- MCN_GETDAYSTATE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCN\_GETDAYSTATE notification code

Sent by a month calendar control to request information about how individual days should be displayed. This notification code is sent only by month calendar controls that use the [**MCS\_DAYSTATE**](month-calendar-control-styles.md) style, and it is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
MCN_GETDAYSTATE

    lpNMDayState = (LPNMDAYSTATE) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMDAYSTATE**](/windows/win32/api/commctrl/ns-commctrl-nmdaystate) structure. The structure contains information about the time frame for which the control needs information, and a stack-allocated array of bitfields to write this data into.

</dd> </dl>

## Return value

No return value.

## Remarks

Handling this notification code allows your application to customize its display by specifying that certain days be displayed in bold.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





