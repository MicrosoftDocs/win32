---
title: RBN\_HEIGHTCHANGE notification code
description: Sent by a rebar control when its height has changed. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: cf90e38c-ac3e-4bef-b047-0956ae5041d1
keywords:
- RBN_HEIGHTCHANGE notification code Windows Controls
topic_type:
- apiref
api_name:
- RBN_HEIGHTCHANGE
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

# RBN\_HEIGHTCHANGE notification code

Sent by a rebar control when its height has changed. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
RBN_HEIGHTCHANGE

    lpnmhdr = (LPNMHDR) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMHDR**](/windows/win32/richedit/ns-richedit-_nmhdr?branch=master) structure that contains additional information about this notification.

</dd> </dl>

## Return value

The return value for this notification is not used.

## Remarks

Rebar controls that use the [**CCS\_VERT**](common-control-styles.md#ccs-vert) style send this notification code when their width changes.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





