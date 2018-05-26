---
title: HDN\_ITEMDBLCLICK notification code
description: Notifies a header controls parent window that the user double-clicked the control. This notification code is sent in the form of a WM\_NOTIFY message. Only header controls that are set to the HDS\_BUTTONS style send this notification code.
ms.assetid: 72bb00b9-226f-4409-b788-b623868f78b6
keywords:
- HDN_ITEMDBLCLICK notification code Windows Controls
topic_type:
- apiref
api_name:
- HDN_ITEMDBLCLICK
- HDN_ITEMDBLCLICKA
- HDN_ITEMDBLCLICKW
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

# HDN\_ITEMDBLCLICK notification code

Notifies a header control's parent window that the user double-clicked the control. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message. Only header controls that are set to the [**HDS\_BUTTONS**](header-control-styles.md#hds-buttons) style send this notification code.


```C++
HDN_ITEMDBLCLICK

    pNMHeader = (LPNMHEADER) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMHEADER**](/windows/win32/Commctrl/ns-commctrl-tagnmheadera?branch=master) structure that contains information about this notification code.

</dd> </dl>

## Return value

No return value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **HDN\_ITEMDBLCLICKW** (Unicode) and **HDN\_ITEMDBLCLICKA** (ANSI)<br/>         |



 

 





