---
title: TVM_SETTOOLTIPS message (Commctrl.h)
description: Sets a tree-view control's child tooltip control. You can send this message explicitly or by using the TreeView\_SetToolTips macro.
ms.assetid: beb9a739-868e-46a8-95d9-9dc032c79dd4
keywords:
- TVM_SETTOOLTIPS message Windows Controls
topic_type:
- apiref
api_name:
- TVM_SETTOOLTIPS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_SETTOOLTIPS message

Sets a tree-view control's child tooltip control. You can send this message explicitly or by using the [**TreeView\_SetToolTips**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_settooltips) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Handle to a tooltip control.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the handle to tooltip control previously set for the tree-view control, or **NULL** if tooltips were not previously used.

## Remarks

When created, tree-view controls automatically create a child tooltip control. To prevent a tree-view control from using tooltips, create the control with the [**TVS\_NOTOOLTIPS**](tree-view-control-window-styles.md) style.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TVM\_GETTOOLTIPS**](tvm-gettooltips.md)
</dt> </dl>

 

 





