---
title: HDN\_ITEMCHANGING notification code
description: Notifies a header controls parent window that the attributes of a header item are about to change. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: c3361f88-69d4-425f-b548-0ad3b2a00af4
keywords:
- HDN_ITEMCHANGING notification code Windows Controls
topic_type:
- apiref
api_name:
- HDN_ITEMCHANGING
- HDN_ITEMCHANGINGA
- HDN_ITEMCHANGINGW
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

# HDN\_ITEMCHANGING notification code

Notifies a header control's parent window that the attributes of a header item are about to change. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
HDN_ITEMCHANGING

    pNMHeader = (LPNMHEADER) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMHEADER**](/windows/win32/Commctrl/ns-commctrl-tagnmheadera?branch=master) structure that contains information about the header control and the header item, including the attributes that are about to change.

</dd> </dl>

## Return value

Returns **FALSE** to allow the changes, or **TRUE** to prevent them.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **HDN\_ITEMCHANGINGW** (Unicode) and **HDN\_ITEMCHANGINGA** (ANSI)<br/>         |



 

 





