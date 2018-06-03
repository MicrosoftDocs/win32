---
title: LVN\_ODFINDITEM message
description: Sent by a virtual list-view control when it needs the owner to find a particular callback item.
ms.assetid: 5a3f9fed-0c57-46bf-b986-ea8b54290b5e
keywords:
- LVN_ODFINDITEM message Windows Controls
topic_type:
- apiref
api_name:
- LVN_ODFINDITEM
- LVN_ODFINDITEMA
- LVN_ODFINDITEMW
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

# LVN\_ODFINDITEM message

Sent by a [virtual list-view](https://www.bing.com/search?q=virtual list-view) control when it needs the owner to find a particular callback item. For example, the control will send this notification code when it receives shortcut keyboard input or when it receives an [**LVM\_FINDITEM**](lvm-finditem.md) message. The LVN\_ODFINDITEM notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
LVN_ODFINDITEM

    pFindInfo = (PNMLVFINDITEM) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMLVFINDITEM**](/windows/desktop/api/Commctrl/ns-commctrl-tagnmlvfinditema) structure that includes information to be used for the search.

</dd> </dl>

## Return value

Return the index of the item found, or -1 if no item is found.

## Remarks

Search information is sent in the form of an [**LVFINDINFO**](/windows/desktop/api/Commctrl/ns-commctrl-taglvfindinfoa) structure, which is a member of the [**NMLVFINDITEM**](/windows/desktop/api/Commctrl/ns-commctrl-tagnmlvfinditema) structure.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **LVN\_ODFINDITEMW** (Unicode) and **LVN\_ODFINDITEMA** (ANSI)<br/>             |



 

 





