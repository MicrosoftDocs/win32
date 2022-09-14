---
title: DL_DRAGGING notification code (Commctrl.h)
description: Signals that the user has moved the mouse while dragging an item.
ms.assetid: 87fc4c24-8e88-4e3c-8f54-ecc7f80de5d7
keywords:
- DL_DRAGGING notification code Windows Controls
topic_type:
- apiref
api_name:
- DL_DRAGGING
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DL\_DRAGGING notification code

Signals that the user has moved the mouse while dragging an item. DL\_DRAGGING is also sent periodically during dragging even if the mouse is not moved. A drag list box sends this notification code to its parent window in the form of a drag list message. For more information, see [Drag List Box Messages](about-list-boxes.md).


```C++
DL_DRAGGING

    pDragInfo = (LPARAM)(LPDRAGLISTINFO) lParam; 
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The control identifier of the drag list box.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**DRAGLISTINFO**](/windows/win32/api/commctrl/ns-commctrl-draglistinfo) structure that contains the DL\_DRAGGING notification code, the handle to the drag list box, and the cursor position.

</dd> </dl>

## Return value

The return value determines the type of mouse cursor that the drag list should set; it can be the DL\_STOPCURSOR, DL\_COPYCURSOR, or DL\_MOVECURSOR value. If any other value is returned, the cursor does not change.

## Remarks

A window procedure typically processes the DL\_DRAGGING notification code by determining the item under the cursor and then drawing an insert icon. To retrieve the item under the cursor, use the [**LBItemFromPt**](/windows/desktop/api/Commctrl/nf-commctrl-lbitemfrompt) function, specifying **TRUE** for the *bAutoScroll* parameter. This option causes the drag list box to scroll periodically if the cursor is above or below its client area. To draw the insert icon, use the [**DrawInsert**](/windows/desktop/api/Commctrl/nf-commctrl-drawinsert) function.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





