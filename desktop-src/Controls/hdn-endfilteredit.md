---
title: HDN_ENDFILTEREDIT notification code
description: Notifies a header control's parent window that a filter edit has ended. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: d3832875-4cde-4d8a-b3a4-a8dae0742c56
keywords:
- HDN_ENDFILTEREDIT notification code Windows Controls
topic_type:
- apiref
api_name:
- HDN_ENDFILTEREDIT
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

# HDN\_ENDFILTEREDIT notification code

Notifies a header control's parent window that a filter edit has ended. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
HDN_ENDFILTEREDIT

   pNMHeader = (LPNMHEADER) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMHEADER**](/windows/desktop/api/Commctrl/ns-commctrl-tagnmheadera) structure that contains additional information about the filter that is being edited.

</dd> </dl>

## Return value

No return value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





