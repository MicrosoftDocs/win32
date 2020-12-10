---
title: LVM_REDRAWITEMS message (Commctrl.h)
description: Forces a list-view control to redraw a range of items. You can send this message explicitly or by using the ListView\_RedrawItems macro.
ms.assetid: a717b17f-6e0a-4804-96f9-da93392a19ec
keywords:
- LVM_REDRAWITEMS message Windows Controls
topic_type:
- apiref
api_name:
- LVM_REDRAWITEMS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_REDRAWITEMS message

Forces a list-view control to redraw a range of items. You can send this message explicitly or by using the [**ListView\_RedrawItems**](/windows/desktop/api/Commctrl/nf-commctrl-listview_redrawitems) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Index of the first item to redraw.

</dd> <dt>

*lParam* 
</dt> <dd>

Index of the last item to redraw.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

The specified items are not actually redrawn until the list-view window receives a [**WM\_PAINT**](/windows/desktop/gdi/wm-paint) message to repaint. To repaint immediately, call the [**UpdateWindow**](/windows/desktop/api/winuser/nf-winuser-updatewindow) function after using this macro.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

