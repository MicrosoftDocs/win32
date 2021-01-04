---
title: LVM_ENSUREVISIBLE message (Commctrl.h)
description: Ensures that a list-view item is either entirely or partially visible, scrolling the list-view control if necessary. You can send this message explicitly or by using the ListView\_EnsureVisible macro.
ms.assetid: 3564b6e6-b8b6-401b-85bc-8bd6261fc054
keywords:
- LVM_ENSUREVISIBLE message Windows Controls
topic_type:
- apiref
api_name:
- LVM_ENSUREVISIBLE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_ENSUREVISIBLE message

Ensures that a list-view item is either entirely or partially visible, scrolling the list-view control if necessary. You can send this message explicitly or by using the [**ListView\_EnsureVisible**](/windows/desktop/api/Commctrl/nf-commctrl-listview_ensurevisible) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The index of the list-view item.

</dd> <dt>

*lParam* 
</dt> <dd>

A value specifying whether the item must be entirely visible. If this parameter is **TRUE**, no scrolling occurs if the item is at least partially visible.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

The message fails if the window style includes [**LVS\_NOSCROLL**](list-view-window-styles.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





