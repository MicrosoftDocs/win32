---
title: TBN_ENDADJUST notification code (Commctrl.h)
description: Notifies a toolbar's parent window that the user has stopped customizing a toolbar. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 9a7496ec-787d-4571-8eca-50d60383519b
keywords:
- TBN_ENDADJUST notification code Windows Controls
topic_type:
- apiref
api_name:
- TBN_ENDADJUST
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBN\_ENDADJUST notification code

Notifies a toolbar's parent window that the user has stopped customizing a toolbar. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TBN_ENDADJUST 

    lpnmhdr = (LPNMHDR) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) structure that contains information about the notification code.

</dd> </dl>

## Return value

No return value.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





