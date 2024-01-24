---
title: HDN_ITEMCHANGED notification code (Commctrl.h)
description: Notifies a header control's parent window that the attributes of a header item have changed. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: ab707010-8ed2-4575-8233-8a1f5656e498
keywords:
- HDN_ITEMCHANGED notification code Windows Controls
topic_type:
- apiref
api_name:
- HDN_ITEMCHANGED
- HDN_ITEMCHANGEDA
- HDN_ITEMCHANGEDW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# HDN\_ITEMCHANGED notification code

Notifies a header control's parent window that the attributes of a header item have changed. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
HDN_ITEMCHANGED

    pNMHeader = (LPNMHEADER) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMHEADER**](/windows/win32/api/commctrl/ns-commctrl-nmheadera) structure that contains information about the header control, including the attributes that have changed.

</dd> </dl>

## Return value

No return value.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **HDN\_ITEMCHANGEDW** (Unicode) and **HDN\_ITEMCHANGEDA** (ANSI)<br/>           |



 

 





