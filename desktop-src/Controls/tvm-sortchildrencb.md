---
title: TVM\_SORTCHILDRENCB message
description: Sorts tree-view items using an application-defined callback function that compares the items. You can send this message explicitly or by using the TreeView\_SortChildrenCB macro.
ms.assetid: 1669e576-5e57-49f6-8097-7d6547306014
keywords:
- TVM_SORTCHILDRENCB message Windows Controls
topic_type:
- apiref
api_name:
- TVM_SORTCHILDRENCB
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TVM\_SORTCHILDRENCB message

Sorts tree-view items using an application-defined callback function that compares the items. You can send this message explicitly or by using the [**TreeView\_SortChildrenCB**](/windows/win32/Commctrl/nf-commctrl-treeview_sortchildrencb?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Reserved. Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TVSORTCB**](/windows/win32/Commctrl/ns-commctrl-tagtvsortcb?branch=master) structure. The **lpfnCompare** member is the address of the application-defined callback function, which is called during the sort operation each time the relative order of two list items needs to be compared. For more information about the callback function, see the description of **TVSORTCB**.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





