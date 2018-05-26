---
title: LVN\_KEYDOWN notification code
description: Notifies a list-view controls parent window that a key has been pressed. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 3aa3d165-7227-41c4-8bc2-3e51a0f52ee3
keywords:
- LVN_KEYDOWN notification code Windows Controls
topic_type:
- apiref
api_name:
- LVN_KEYDOWN
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

# LVN\_KEYDOWN notification code

Notifies a list-view control's parent window that a key has been pressed. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
LVN_KEYDOWN

    pnkd = (LPNMLVKEYDOWN) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMLVKEYDOWN**](/windows/win32/Commctrl/ns-commctrl-taglvkeydown?branch=master) structure.

</dd> </dl>

## Return value

No return value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





