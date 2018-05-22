---
title: LVN\_INSERTITEM notification code
description: Notifies a list-view control's parent window that a new item was inserted. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: '8d368fb2-e4fc-4dc4-a89e-872ba1278b75'
keywords: ["LVN_INSERTITEM notification code Windows Controls"]
topic_type:
- apiref
api_name:
- LVN_INSERTITEM
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# LVN\_INSERTITEM notification code

Notifies a list-view control's parent window that a new item was inserted. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
LVN_INSERTITEM

    pnmv = (LPNMLISTVIEW) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMLISTVIEW**](nmlistview.md) structure. The **iItem** member identifies the new item, and the other members are zero.

</dd> </dl>

## Return value

No return value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





