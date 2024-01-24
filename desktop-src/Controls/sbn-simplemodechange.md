---
title: SBN_SIMPLEMODECHANGE notification code (Commctrl.h)
description: Sent by a status bar control when the simple mode changes due to a SB\_SIMPLE message. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: b2df8feb-5028-4488-a99b-4ceff5b48a92
keywords:
- SBN_SIMPLEMODECHANGE notification code Windows Controls
topic_type:
- apiref
api_name:
- SBN_SIMPLEMODECHANGE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SBN\_SIMPLEMODECHANGE notification code

Sent by a status bar control when the simple mode changes due to a [**SB\_SIMPLE**](sb-simple.md) message. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
SBN_SIMPLEMODECHANGE

    lpnmh = (NMHDR*) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) structure that contains information about the notification code.

</dd> </dl>

## Return value

The return value is ignored by the status bar.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





