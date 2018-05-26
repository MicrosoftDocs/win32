---
title: CBEN\_GETDISPINFO notification code
description: Sent to retrieve display information about a callback item. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: a181be28-0001-4953-8e59-77aff2dc40be
keywords:
- CBEN_GETDISPINFO notification code Windows Controls
topic_type:
- apiref
api_name:
- CBEN_GETDISPINFO
- CBEN_GETDISPINFOA
- CBEN_GETDISPINFOW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBEN\_GETDISPINFO notification code

Sent to retrieve display information about a callback item. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
CBEN_GETDISPINFO

    pDispInfo = (PNMCOMBOBOXEX) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMCOMBOBOXEX**](/windows/win32/Commctrl/ns-commctrl-nmcomboboxexa?branch=master) structure that contains information about the notification code.

</dd> </dl>

## Return value

The application processing this notification code must return zero.

## Remarks

The [**NMCOMBOBOXEX**](/windows/win32/Commctrl/ns-commctrl-nmcomboboxexa?branch=master) structure contains a [**COMBOBOXEXITEM**](/windows/win32/Commctrl/ns-commctrl-tagcomboboxexitema?branch=master) structure. The **mask** member specifies the information being requested by the control.

Fill the appropriate members of the structure to return the requested information to the control. If your message handler sets the **mask** member of the [**COMBOBOXEXITEM**](/windows/win32/Commctrl/ns-commctrl-tagcomboboxexitema?branch=master) structure to CBEIF\_DI\_SETITEM, the control stores the information and will not request it again.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **CBEN\_GETDISPINFOW** (Unicode) and **CBEN\_GETDISPINFOA** (ANSI)<br/>         |



 

 





