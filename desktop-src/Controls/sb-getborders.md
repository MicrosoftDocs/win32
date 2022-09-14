---
title: SB_GETBORDERS message (Commctrl.h)
description: Retrieves the current widths of the horizontal and vertical borders of a status window.
ms.assetid: 120c1e0d-6f42-424e-94e0-a080d216d39d
keywords:
- SB_GETBORDERS message Windows Controls
topic_type:
- apiref
api_name:
- SB_GETBORDERS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SB\_GETBORDERS message

Retrieves the current widths of the horizontal and vertical borders of a status window.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to an integer array that has three elements. The first element receives the width of the horizontal border, the second receives the width of the vertical border, and the third receives the width of the border between rectangles.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

The borders determine the spacing between the outside edge of the window and the rectangles within the window that contain text. The borders also determine the spacing between rectangles.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





