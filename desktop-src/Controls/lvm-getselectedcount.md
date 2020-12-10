---
title: LVM_GETSELECTEDCOUNT message (Commctrl.h)
description: Determines the number of selected items in a list-view control. You can send this message explicitly or by using the ListView\_GetSelectedCount macro.
ms.assetid: 38916227-e6ca-4efa-9821-13f0fdb29834
keywords:
- LVM_GETSELECTEDCOUNT message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETSELECTEDCOUNT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETSELECTEDCOUNT message

Determines the number of selected items in a list-view control. You can send this message explicitly or by using the [**ListView\_GetSelectedCount**](/windows/desktop/api/Commctrl/nf-commctrl-listview_getselectedcount) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the number of selected items.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





