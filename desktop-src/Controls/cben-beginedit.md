---
title: CBEN\_BEGINEDIT notification code
description: Sent when the user activates the drop-down list or clicks in the controls edit box. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 77236471-b1c0-4679-b7b8-93e85867fe3b
keywords:
- CBEN_BEGINEDIT notification code Windows Controls
topic_type:
- apiref
api_name:
- CBEN_BEGINEDIT
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

# CBEN\_BEGINEDIT notification code

Sent when the user activates the drop-down list or clicks in the control's edit box. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
CBEN_BEGINEDIT

    lpnmhdr = (LPNMHDR) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMHDR**](/windows/win32/richedit/ns-richedit-_nmhdr?branch=master) structure that contains information about the notification code.

</dd> </dl>

## Return value

The application processing this notification code must return zero.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





