---
title: UDN_DELTAPOS notification code
description: Sent by the operating system to the parent window of an up-down control when the position of the control is about to change.
ms.assetid: 66262566-d35a-4b2a-8157-d1e789a21016
keywords:
- UDN_DELTAPOS notification code Windows Controls
topic_type:
- apiref
api_name:
- UDN_DELTAPOS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# UDN\_DELTAPOS notification code

Sent by the operating system to the parent window of an up-down control when the position of the control is about to change. This happens when the user requests a change in the value by pressing the control's up or down arrow. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
UDN_DELTAPOS 

    lpnmud = (LPNMUPDOWN) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMUPDOWN**](/windows/desktop/api/Commctrl/ns-commctrl-_nm_updown) structure that contains information about the position change. The **iPos** member of this structure contains the current position of the control. The **iDelta** member of the structure is a signed integer that contains the proposed change in position. If the user has clicked the up button, this is a positive value. If the user has clicked the down button, this is a negative value.

</dd> </dl>

## Return value

Return nonzero to prevent the change in the control's position, or zero to allow the change.

## Remarks

The UDN\_DELTAPOS notification code is sent before the [**WM\_VSCROLL**](wm-vscroll.md) or [**WM\_HSCROLL**](wm-hscroll.md) message, which actually changes the control's position. This lets you examine, allow, modify, or disallow the change.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591)
</dt> </dl>

 

 





