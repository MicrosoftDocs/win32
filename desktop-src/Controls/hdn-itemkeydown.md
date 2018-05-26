---
title: HDN\_ITEMKEYDOWN notification code
description: Notifies a header controls parent window that a key has been pressed with an item selected. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: ab6922ab-907d-44fc-8606-28f395118405
keywords:
- HDN_ITEMKEYDOWN notification code Windows Controls
topic_type:
- apiref
api_name:
- HDN_ITEMKEYDOWN
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

# HDN\_ITEMKEYDOWN notification code

Notifies a header control's parent window that a key has been pressed with an item selected. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
HDN_ITEMKEYDOWN

   pNMHeader = (LPNMHEADER) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMHEADER**](/windows/win32/Commctrl/ns-commctrl-tagnmheadera?branch=master) structure that contains additional information about the key that is being pressed.

</dd> </dl>

## Return value

No return value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





