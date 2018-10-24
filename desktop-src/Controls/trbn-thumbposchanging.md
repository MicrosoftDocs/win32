---
title: TRBN_THUMBPOSCHANGING notification code
description: Notifies that the thumb position on a trackbar is changing. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 0876e026-bc07-409d-b174-b97ed704fc11
keywords:
- TRBN_THUMBPOSCHANGING notification code Windows Controls
topic_type:
- apiref
api_name:
- TRBN_THUMBPOSCHANGING
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TRBN\_THUMBPOSCHANGING notification code

Notifies that the thumb position on a trackbar is changing. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TRBN_THUMBPOSCHANGING

    lpNMTrbThumbPosChanging = (NMTRBTHUMBPOSCHANGING*) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**NMTRBTHUMBPOSCHANGING**](/windows/desktop/api/Commctrl/ns-commctrl-tagtrbthumbposchanging) structure. The caller is responsible for allocating this structure and setting its members, including the members of the contained [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-_nmhdr) structure.

</dd> </dl>

## Return value

The return value is ignored.

## Remarks

Send this notification to clients that do not listen for [**WM\_HSCROLL**](wm-hscroll.md) or [**WM\_VSCROLL**](wm-vscroll.md) messages.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





