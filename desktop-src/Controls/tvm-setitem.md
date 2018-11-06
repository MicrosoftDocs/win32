---
title: TVM_SETITEM message
description: The TVM\_SETITEM message sets some or all of a tree-view item's attributes. You can send this message explicitly or by using the TreeView\_SetItem macro.
ms.assetid: 28d288bf-a557-4fce-870c-ffa368ece5a9
keywords:
- TVM_SETITEM message Windows Controls
topic_type:
- apiref
api_name:
- TVM_SETITEM
- TVM_SETITEMA
- TVM_SETITEMW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: article
ms.date: 05/31/2018
---

# TVM\_SETITEM message

The **TVM\_SETITEM** message sets some or all of a tree-view item's attributes. You can send this message explicitly or by using the [**TreeView\_SetItem**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_setitem) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TVITEM**](/windows/desktop/api/Commctrl/ns-commctrl-tagtvitema) structure that contains the new item attributes. With [version 4.71](common-control-versions.md) and later, you can use a [**TVITEMEX**](/windows/desktop/api/Commctrl/ns-commctrl-tagtvitemexa) structure instead.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

The **hItem** member of the [**TVITEM**](/windows/desktop/api/Commctrl/ns-commctrl-tagtvitema) or [**TVITEMEX**](/windows/desktop/api/Commctrl/ns-commctrl-tagtvitemexa) structure identifies the item, and the **mask** member specifies which attributes to set.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TVM\_SETITEMW** (Unicode) and **TVM\_SETITEMA** (ANSI)<br/>                   |



 

 





