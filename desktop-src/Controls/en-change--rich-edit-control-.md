---
title: EN\_CHANGE (rich edit) notification code
description: Notifies a windowless rich edit controls host window that a change has occurred. A rich edit control sends this notification code in the form of a WM\_NOTIFY message.
ms.assetid: 97C0D9F1-7D4E-409D-A4F6-E645475A8EEF
keywords:
- EN_CHANGE (rich edit) notification code Windows Controls
topic_type:
- apiref
api_name:
- EN_CHANGE (rich edit control)
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EN\_CHANGE (rich edit) notification code

Notifies a windowless rich edit control's host window that a change has occurred. A rich edit control sends this notification code in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
EN_CHANGE

    penChangeNotify = (CHANGENOTIFY *) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A [**CHANGENOTIFY**](/windows/win32/Textserv/ns-textserv-changenotify?branch=master) structure specifying the change that was made.

</dd> </dl>

## Return value

This notification code does not return a value.

## Remarks

To receive EN\_CHANGE notification codes, specify [**ENM\_CHANGE**](rich-edit-control-event-mask-flags.md#enm-change) in the mask sent with the [**EM\_SETEVENTMASK**](em-seteventmask.md) message.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Winuser.h</dt> </dl> |



## See also

<dl> <dt>

[**TxNotify**](/windows/win32/Textserv/nf-textserv-itexthost-txnotify?branch=master)
</dt> </dl>

 

 





