---
title: TCN_KEYDOWN notification code (Commctrl.h)
description: Notifies a tab control's parent window that a key has been pressed. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 884e79cd-5732-44cd-8c7a-38bb9349ec7d
keywords:
- TCN_KEYDOWN notification code Windows Controls
topic_type:
- apiref
api_name:
- TCN_KEYDOWN
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TCN\_KEYDOWN notification code

Notifies a tab control's parent window that a key has been pressed. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TCN_KEYDOWN 

    pnm = (NMTCKEYDOWN*) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTCKEYDOWN**](/windows/win32/api/commctrl/ns-commctrl-nmtckeydown) structure.

</dd> </dl>

## Return value

No return value.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





