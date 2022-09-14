---
title: DL_CANCELDRAG notification code (Commctrl.h)
description: Signals that the user has canceled a drag operation by clicking the right mouse button or pressing the ESC key.
ms.assetid: 62c1377f-41b6-449f-a95e-2689dc1913c6
keywords:
- DL_CANCELDRAG notification code Windows Controls
topic_type:
- apiref
api_name:
- DL_CANCELDRAG
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DL\_CANCELDRAG notification code

Signals that the user has canceled a drag operation by clicking the right mouse button or pressing the ESC key. A drag list box sends this notification code to its parent window in the form of a drag list message. For more information, see [Drag List Box Messages](about-list-boxes.md).


```C++
DL_CANCELDRAG

    pDragInfo = (LPARAM)(LPDRAGLISTINFO) lParam;
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**DRAGLISTINFO**](/windows/win32/api/commctrl/ns-commctrl-draglistinfo) structure that contains the DL\_CANCELDRAG notification code, the handle to the drag list box, and the cursor position.

</dd> </dl>

## Return value

No return value.

## Remarks

By processing the DL\_CANCELDRAG notification code, an application can reset its internal state to indicate that dragging is not in effect.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





