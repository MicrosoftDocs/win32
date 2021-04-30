---
title: LVM_GETHOTCURSOR message (Commctrl.h)
description: Retrieves the HCURSOR value used when the pointer is over an item while hot tracking is enabled. You can send this message explicitly or use the ListView\_GetHotCursor macro.
ms.assetid: 064d04b2-d74e-4a80-aec6-97a3c53fc4fb
keywords:
- LVM_GETHOTCURSOR message Windows Controls
topic_type:
- apiref
api_name:
- LVM_GETHOTCURSOR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_GETHOTCURSOR message

Retrieves the HCURSOR value used when the pointer is over an item while hot tracking is enabled. You can send this message explicitly or use the [**ListView\_GetHotCursor**](/windows/desktop/api/Commctrl/nf-commctrl-listview_gethotcursor) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns an HCURSOR value that is the handle to the cursor that the list-view control uses when hot tracking is enabled.

## Remarks

A list-view control uses hot tracking and hover selection when the [**LVS\_EX\_TRACKSELECT**](extended-list-view-styles.md) style is set.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





