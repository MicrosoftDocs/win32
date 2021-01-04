---
title: TVM_SETITEMHEIGHT message (Commctrl.h)
description: Sets the height of the tree-view items. You can send this message explicitly or by using the TreeView\_SetItemHeight macro.
ms.assetid: 23f6f2a4-cdd9-441d-af24-ed40513d2721
keywords:
- TVM_SETITEMHEIGHT message Windows Controls
topic_type:
- apiref
api_name:
- TVM_SETITEMHEIGHT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_SETITEMHEIGHT message

Sets the height of the tree-view items. You can send this message explicitly or by using the [**TreeView\_SetItemHeight**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_setitemheight) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

New height of every item in the tree view, in pixels. Heights less than 1 will be set to 1. If this argument is not even and the tree-view control does not have the [**TVS\_NONEVENHEIGHT**](tree-view-control-window-styles.md) style, this value will be rounded down to the nearest even value. If this argument is -1, the control will revert to using its default item height.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the previous height of the items, in pixels.

## Remarks

The tree-view control uses this value for the height of all items. To modify the height of individual items, see the description of the **iIntegral** member of the [**TVITEMEX**](/windows/win32/api/commctrl/ns-commctrl-tvitemexa) structure.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TVM\_GETITEMHEIGHT**](tvm-getitemheight.md)
</dt> </dl>

 

 





