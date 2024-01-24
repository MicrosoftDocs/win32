---
title: LVN_GETEMPTYMARKUP notification code (Commctrl.h)
description: Sent by list-view control to its parent window when the control has no items. The LVN\_GETEMPTYMARKUP notification code is a request for the parent window to provide markup text. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 5ea74120-f347-493a-af14-6bda5b8f6082
keywords:
- LVN_GETEMPTYMARKUP notification code Windows Controls
topic_type:
- apiref
api_name:
- LVN_GETEMPTYMARKUP
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVN\_GETEMPTYMARKUP notification code

Sent by list-view control to its parent window when the control has no items. The LVN\_GETEMPTYMARKUP notification code is a request for the parent window to provide markup text. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
LVN_GETEMPTYMARKUP
        
    pnmMarkup = (NMLVEMPTYMARKUP*) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**NMLVEMPTYMARKUP**](/windows/win32/api/commctrl/ns-commctrl-nmlvemptymarkup) structure. Set the members of this structure to provide markup text for the list-view control.

</dd> </dl>

## Return value

Return **TRUE** to set the markup text in the list-view control, or **FALSE** otherwise.

## Remarks

The notification receiver casts *lParam* to retrieve the [**NMLVEMPTYMARKUP**](/windows/win32/api/commctrl/ns-commctrl-nmlvemptymarkup) structure. The *wParam* parameter contains the ID of the control that sends this message.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





