---
title: EN\_PARAGRAPHEXPANDED notification code
description: Notifies a rich edit controls parent that an outline has been expanded. A rich edit control sends this notification code in the form of a WM\_NOTIFY message.
ms.assetid: D33EB118-FC79-4284-820B-3424F13722C4
keywords:
- EN_PARAGRAPHEXPANDED notification code Windows Controls
topic_type:
- apiref
api_name:
- EN_PARAGRAPHEXPANDEDC
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EN\_PARAGRAPHEXPANDED notification code

Notifies a rich edit control's parent that an outline has been expanded. A rich edit control sends this notification code in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
EN_PARAGRAPHEXPANDED

    lpnmhdr = (LPNMHDR) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

An [**NMHDR**](/windows/win32/richedit/ns-richedit-_nmhdr?branch=master) structure.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



 

 





