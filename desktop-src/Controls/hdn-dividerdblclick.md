---
title: HDN\_DIVIDERDBLCLICK notification code
description: Notifies a header controls parent window that the user double-clicked the divider area of the control. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: b722196a-23ae-49c3-b0a2-8fe0d1e33b26
keywords:
- HDN_DIVIDERDBLCLICK notification code Windows Controls
topic_type:
- apiref
api_name:
- HDN_DIVIDERDBLCLICK
- HDN_DIVIDERDBLCLICKA
- HDN_DIVIDERDBLCLICKW
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

# HDN\_DIVIDERDBLCLICK notification code

Notifies a header control's parent window that the user double-clicked the divider area of the control. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
HDN_DIVIDERDBLCLICK

    pNMHeader = (LPNMHEADER) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMHEADER**](/windows/win32/Commctrl/ns-commctrl-tagnmheadera?branch=master) structure that contains information about the header control and the item whose divider was double-clicked.

</dd> </dl>

## Return value

No return value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **HDN\_DIVIDERDBLCLICKW** (Unicode) and **HDN\_DIVIDERDBLCLICKA** (ANSI)<br/>   |



 

 





