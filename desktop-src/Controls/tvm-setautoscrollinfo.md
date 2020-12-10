---
title: TVM_SETAUTOSCROLLINFO message (Commctrl.h)
description: Sets information used to determine auto-scroll characteristics. You can send this message explicitly or by using the TreeView\_SetAutoScrollInfo macro.
ms.assetid: de55933f-1caa-4193-84de-0486c41e8f1f
keywords:
- TVM_SETAUTOSCROLLINFO message Windows Controls
topic_type:
- apiref
api_name:
- TVM_SETAUTOSCROLLINFO
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_SETAUTOSCROLLINFO message

Sets information used to determine auto-scroll characteristics. You can send this message explicitly or by using the [**TreeView\_SetAutoScrollInfo**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_setautoscrollinfo) macro.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

Specifies pixels per second. The offset to scroll is divided by the *wParam* to determine the total duration of the auto-scroll.

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

Specifies the redraw time interval. Redraw at every elasped interval, until the item is scrolled into view. Given *wParam*, the location of the item is calculated and a repaint occurs. Set this value to create smooth scrolling.

</dd> </dl>

## Return value

Returns **TRUE**.

## Remarks

Autoscroll information is used to scroll a nonvisible item into view. The control must have the [**TVS\_EX\_AUTOHSCROLL**](tree-view-control-window-extended-styles.md) extended style. For information on extended styles, see Tree-View Control Extended Styles.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





