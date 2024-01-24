---
title: TVM_GETTOOLTIPS message (Commctrl.h)
description: Retrieves the handle to the child tooltip control used by a tree-view control. You can send this message explicitly or by using the TreeView\_GetToolTips macro.
ms.assetid: 65e8189e-ae3e-4268-b1ed-bb0d88f2cbe3
keywords:
- TVM_GETTOOLTIPS message Windows Controls
topic_type:
- apiref
api_name:
- TVM_GETTOOLTIPS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_GETTOOLTIPS message

Retrieves the handle to the child tooltip control used by a tree-view control. You can send this message explicitly or by using the [**TreeView\_GetToolTips**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_gettooltips) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the handle to the child tooltip control, or **NULL** if the control is not using tooltips.

## Remarks

When created, tree-view controls automatically create a child tooltip control. To cause a tree-view control not to use tooltips, create the control with the [**TVS\_NOTOOLTIPS**](tree-view-control-window-styles.md) style.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TVM\_SETTOOLTIPS**](tvm-settooltips.md)
</dt> </dl>

 

 





