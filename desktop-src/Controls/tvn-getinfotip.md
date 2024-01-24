---
title: TVN_GETINFOTIP notification code (Commctrl.h)
description: Sent by a tree-view control that has the TVS\_INFOTIP style. This notification code is sent when the control is requesting additional text information to be displayed in a tooltip. The notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 20576710-e279-4e61-be6b-bf1d8ea79555
keywords:
- TVN_GETINFOTIP notification code Windows Controls
topic_type:
- apiref
api_name:
- TVN_GETINFOTIP
- TVN_GETINFOTIPA
- TVN_GETINFOTIPW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVN\_GETINFOTIP notification code

Sent by a tree-view control that has the [**TVS\_INFOTIP**](tree-view-control-window-styles.md) style. This notification code is sent when the control is requesting additional text information to be displayed in a tooltip. The notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TVN_GETINFOTIP

    lpGetInfoTip = (LPNMTVGETINFOTIP)lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTVGETINFOTIP**](/windows/win32/api/commctrl/ns-commctrl-nmtvgetinfotipa) structure that contains information about this notification code.

</dd> </dl>

## Return value

The control ignores the return value for this notification code.

## Remarks

This notification code is only sent by tree-view controls that have the [**TVS\_INFOTIP**](tree-view-control-window-styles.md) style.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TVN\_GETINFOTIPW** (Unicode) and **TVN\_GETINFOTIPA** (ANSI)<br/>             |



 

 





