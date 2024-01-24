---
title: DL_BEGINDRAG notification code (Commctrl.h)
description: Notifies the drag list box's parent window that the user has clicked the left mouse button on an item. A drag list box sends this notification code in the form of a drag list message. For more information, see Drag List Box Messages.
ms.assetid: ccf66818-e5f7-4165-8d0d-4d279944f70e
keywords:
- DL_BEGINDRAG notification code Windows Controls
topic_type:
- apiref
api_name:
- DL_BEGINDRAG
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DL\_BEGINDRAG notification code

Notifies the drag list box's parent window that the user has clicked the left mouse button on an item. A drag list box sends this notification code in the form of a drag list message. For more information, see [Drag List Box Messages](about-list-boxes.md).


```C++
DL_BEGINDRAG

    pDragInfo = (LPARAM)(LPDRAGLISTINFO) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**DRAGLISTINFO**](/windows/win32/api/commctrl/ns-commctrl-draglistinfo) structure that contains the DL\_BEGINDRAG notification code, the handle to the drag list box, and the cursor position.

</dd> </dl>

## Return value

Return **TRUE** to begin the drag operation, or **FALSE** to prevent the drag operation.

## Remarks

When processing this notification code, a window procedure typically determines the list item at the specified cursor position by using the [**LBItemFromPt**](/windows/desktop/api/Commctrl/nf-commctrl-lbitemfrompt) function. It then returns **TRUE** or **FALSE**, depending on whether the item should be dragged. Before returning **TRUE**, the window procedure should save the index of the list item so the application knows which item to move or copy when the drag operation is completed.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





