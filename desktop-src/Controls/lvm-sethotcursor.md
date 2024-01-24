---
title: LVM_SETHOTCURSOR message (Commctrl.h)
description: Sets the HCURSOR value that the list-view control uses when the pointer is over an item while hot tracking is enabled.
ms.assetid: e3ff8608-9389-4167-839b-ecc2be01bb64
keywords:
- LVM_SETHOTCURSOR message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETHOTCURSOR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_SETHOTCURSOR message

Sets the HCURSOR value that the list-view control uses when the pointer is over an item while hot tracking is enabled. You can send this message explicitly or use the [**ListView\_SetHotCursor**](/windows/desktop/api/Commctrl/nf-commctrl-listview_sethotcursor) macro. To check whether hot tracking is enabled, call [**SystemParametersInfo**](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa).

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the cursor to be set.

</dd> </dl>

## Return value

Returns an HCURSOR value that is the previous hot cursor.

## Remarks

A list-view control uses hot tracking and hover selection when the [**LVS\_EX\_TRACKSELECT**](extended-list-view-styles.md) style is set.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

