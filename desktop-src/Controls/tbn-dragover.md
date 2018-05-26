---
title: TBN\_DRAGOVER notification code
description: Ascertains whether a TB\_MARKBUTTON message should be sent for a button that is being dragged over. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 2bb5c52e-0c90-4662-8ffd-045ecc7ed7e5
keywords:
- TBN_DRAGOVER notification code Windows Controls
topic_type:
- apiref
api_name:
- TBN_DRAGOVER
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

# TBN\_DRAGOVER notification code

Ascertains whether a [**TB\_MARKBUTTON**](tb-markbutton.md) message should be sent for a button that is being dragged over. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TBN_DRAGOVER

    lpnmtb = (NMTBHOTITEM*) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMTBHOTITEM**](/windows/win32/Commctrl/ns-commctrl-tagnmtbhotitem?branch=master) structure that specifies which item is being dragged over.

</dd> </dl>

## Return value

**FALSE** if the toolbar should send a TB\_MARKBUTTON message; otherwise **TRUE**.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





