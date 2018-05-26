---
title: LVN\_BEGINDRAG notification code
description: Notifies a list-view controls parent window that a drag-and-drop operation involving the left mouse button is being initiated. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 2b9bbff8-f5f7-47ac-b662-a327ff49caf7
keywords:
- LVN_BEGINDRAG notification code Windows Controls
topic_type:
- apiref
api_name:
- LVN_BEGINDRAG
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

# LVN\_BEGINDRAG notification code

Notifies a list-view control's parent window that a drag-and-drop operation involving the left mouse button is being initiated. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
LVN_BEGINDRAG

    pnmv = (LPNMLISTVIEW) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMLISTVIEW**](/windows/win32/Commctrl/ns-commctrl-tagnmlistview?branch=master) structure. The **iItem** member identifies the item being dragged, and the other members are zero.

</dd> </dl>

## Return value

No return value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





