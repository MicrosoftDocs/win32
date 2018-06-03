---
title: TVM\_GETITEM message
description: Retrieves some or all of a tree-view item's attributes. You can send this message explicitly or by using the TreeView\_GetItem macro.
ms.assetid: e26ec000-967d-46de-8f71-6ebc36fefe5e
keywords:
- TVM_GETITEM message Windows Controls
topic_type:
- apiref
api_name:
- TVM_GETITEM
- TVM_GETITEMA
- TVM_GETITEMW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TVM\_GETITEM message

Retrieves some or all of a tree-view item's attributes. You can send this message explicitly or by using the [**TreeView\_GetItem**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_getitem) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TVITEM**](/windows/desktop/api/Commctrl/ns-commctrl-tagtvitema) structure that specifies the information to retrieve and receives information about the item. With [version 4.71](common-control-versions.md) and later, you can use a [**TVITEMEX**](/windows/desktop/api/Commctrl/ns-commctrl-tagtvitemexa) structure instead.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

When the message is sent, the **hItem** member of the [**TVITEM**](/windows/desktop/api/Commctrl/ns-commctrl-tagtvitema) or [**TVITEMEX**](/windows/desktop/api/Commctrl/ns-commctrl-tagtvitemexa) structure identifies the item to retrieve information about, and the **mask** member specifies the attributes to retrieve.

If the TVIF\_TEXT flag is set in the **mask** member of the [**TVITEM**](/windows/desktop/api/Commctrl/ns-commctrl-tagtvitema) or [**TVITEMEX**](/windows/desktop/api/Commctrl/ns-commctrl-tagtvitemexa) structure, the **pszText** member must point to a valid buffer and the **cchTextMax** member must be set to the number of characters in that buffer.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TVM\_GETITEMW** (Unicode) and **TVM\_GETITEMA** (ANSI)<br/>                   |



 

 





