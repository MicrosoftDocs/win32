---
title: LVM_SCROLL message (Commctrl.h)
description: Scrolls the content of a list-view control. You can send this message explicitly or by using the ListView\_Scroll macro.
ms.assetid: 4bf6b74e-8fea-48ca-a151-8fd649fc50f8
keywords:
- LVM_SCROLL message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SCROLL
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_SCROLL message

Scrolls the content of a list-view control. You can send this message explicitly or by using the [**ListView\_Scroll**](/windows/desktop/api/Commctrl/nf-commctrl-listview_scroll) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Value of type **int** that specifies the amount of horizontal scrolling, in pixels, relative to the current position of the list view content. If the list-view control is in list view, this value is rounded up to the nearest number of pixels that form a whole column.

</dd> <dt>

*lParam* 
</dt> <dd>

Value of type **int** that specifies the amount of vertical scrolling, in pixels, relative to the current position of the list view content.

</dd> </dl>

## Return value

Returns **TRUE** if successful; otherwise, **FALSE**.

## Remarks

When the list-view control is in report view, the control can only be scrolled vertically in whole line increments. Therefore, the *lParam* parameter will be rounded to the nearest number of pixels that form a whole line increment. For example, if the height of a line is 16 pixels and 8 is passed for *lParam*, the list will be scrolled by 16 pixels (1 line). If 7 is passed for *lParam*, the list will be scrolled 0 pixels (0 lines).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





