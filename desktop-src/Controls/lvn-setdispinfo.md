---
title: LVN_SETDISPINFO notification code (Commctrl.h)
description: Notifies a list-view control's parent window that it must update the information it maintains for an item. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 1ea51d50-4a57-4662-972e-89e916fa9b16
keywords:
- LVN_SETDISPINFO notification code Windows Controls
topic_type:
- apiref
api_name:
- LVN_SETDISPINFO
- LVN_SETDISPINFOA
- LVN_SETDISPINFOW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVN\_SETDISPINFO notification code

Notifies a list-view control's parent window that it must update the information it maintains for an item. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
LVN_SETDISPINFO
        
    pdi = (NMLVDISPINFO*) lParam
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMLVDISPINFO**](/windows/win32/api/commctrl/ns-commctrl-nmlvdispinfoa) structure that specifies information for the changed item. The **item** member of this structure is an [**LVITEM**](/windows/win32/api/commctrl/ns-commctrl-lvitema) structure that contains information about the item that was changed. The **pszText** member of **item** contains a valid value, regardless of whether the LVIF\_TEXT flag is set in the **mask** member of this structure.

</dd> </dl>

## Return value

No return value.

## Remarks

The notification receiver casts *lParam* to retrieve the [**NMLVDISPINFO**](/windows/win32/api/commctrl/ns-commctrl-nmlvdispinfoa) structure. The *wParam* parameter contains the message code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **LVN\_SETDISPINFOW** (Unicode) and **LVN\_SETDISPINFOA** (ANSI)<br/>           |



## See also

<dl> <dt>

[LVN\_GETDISPINFO](lvn-getdispinfo.md)
</dt> </dl>

 

 





