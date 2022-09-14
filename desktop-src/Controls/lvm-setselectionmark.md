---
title: LVM_SETSELECTIONMARK message (Commctrl.h)
description: Sets the selection mark in a list-view control. You can send this message explicitly or use the ListView\_SetSelectionMark macro.
ms.assetid: 3218f1b3-b934-4083-aaaa-e10ef1dbb6bd
keywords:
- LVM_SETSELECTIONMARK message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETSELECTIONMARK
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_SETSELECTIONMARK message

Sets the selection mark in a list-view control. You can send this message explicitly or use the [**ListView\_SetSelectionMark**](/windows/desktop/api/Commctrl/nf-commctrl-listview_setselectionmark) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Zero-based index of the new selection mark. If set to -1, the selection mark is removed.

</dd> </dl>

## Return value

Returns the previous selection mark, or -1 if there is no previous selection mark.

## Remarks

The *selection mark* is the item index from which a multiple selection starts. This message does not affect the selection state of the item.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**LVM\_GETSELECTIONMARK**](lvm-getselectionmark.md)
</dt> </dl>

 

 





