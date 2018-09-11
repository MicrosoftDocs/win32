---
title: LVN_ENDSCROLL message
description: Notifies a list-view control's parent window when a scrolling operation ends. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 2838dcd0-ac0f-48c7-94ba-dc36febedb94
keywords:
- LVN_ENDSCROLL message Windows Controls
topic_type:
- apiref
api_name:
- LVN_ENDSCROLL
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LVN\_ENDSCROLL message

Notifies a list-view control's parent window when a scrolling operation ends. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
LVN_ENDSCROLL

    pnmLVScroll = (LPNMLVSCROLL) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**NMLVSCROLL**](/windows/desktop/api/Commctrl/ns-commctrl-tagnmlvscroll) structure that contains the horizontal or vertical position of where the scroll operation ends.

</dd> </dl>

## Return value

Return value not used.

## Remarks

> [!Note]  
> To use this notification code, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





