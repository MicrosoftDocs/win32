---
title: DTN_DATETIMECHANGE notification code (Commctrl.h)
description: Sent by a date and time picker (DTP) control whenever a change occurs. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 65cdd8fb-1f07-4447-b503-d40fdfa37202
keywords:
- DTN_DATETIMECHANGE notification code Windows Controls
topic_type:
- apiref
api_name:
- DTN_DATETIMECHANGE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DTN\_DATETIMECHANGE notification code

Sent by a date and time picker (DTP) control whenever a change occurs. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
DTN_DATETIMECHANGE

    lpChange = (LPNMDATETIMECHANGE) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMDATETIMECHANGE**](/windows/win32/api/commctrl/ns-commctrl-nmdatetimechange) structure containing information about the change that took place in the control.

</dd> </dl>

## Return value

The owner of the control must return zero.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





