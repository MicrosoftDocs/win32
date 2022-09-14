---
title: DTN_WMKEYDOWN notification code (Commctrl.h)
description: Sent by a date and time picker (DTP) control when the user types in a callback field. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: e67e222d-28a1-4d30-ae64-8ec9a62fa321
keywords:
- DTN_WMKEYDOWN notification code Windows Controls
topic_type:
- apiref
api_name:
- DTN_WMKEYDOWN
- DTN_WMKEYDOWNA
- DTN_WMKEYDOWNW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DTN\_WMKEYDOWN notification code

Sent by a date and time picker (DTP) control when the user types in a callback field. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
DTN_WMKEYDOWN

    lpDTKeystroke = (LPNMDATETIMEWMKEYDOWN)lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMDATETIMEWMKEYDOWN**](/windows/win32/api/commctrl/ns-commctrl-nmdatetimewmkeydowna) structure containing information about this instance of the notification code. The structure includes information about the key that the user typed, the substring that defines the callback field, and the current system date and time.

</dd> </dl>

## Return value

The owner of the control must return zero.

## Remarks

Handling this notification code allows the owner of the control to provide specific responses to keystrokes within the callback fields of the control.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **DTN\_WMKEYDOWNW** (Unicode) and **DTN\_WMKEYDOWNA** (ANSI)<br/>               |



 

 





