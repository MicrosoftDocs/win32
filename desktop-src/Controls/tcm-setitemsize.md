---
title: TCM_SETITEMSIZE message (Commctrl.h)
description: Sets the width and height of tabs in a fixed-width or owner-drawn tab control. You can send this message explicitly or by using the TabCtrl\_SetItemSize macro.
ms.assetid: 3935d686-f8bc-41fb-b025-04120cf03f02
keywords:
- TCM_SETITEMSIZE message Windows Controls
topic_type:
- apiref
api_name:
- TCM_SETITEMSIZE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TCM\_SETITEMSIZE message

Sets the width and height of tabs in a fixed-width or owner-drawn tab control. You can send this message explicitly or by using the [**TabCtrl\_SetItemSize**](/windows/desktop/api/Commctrl/nf-commctrl-tabctrl_setitemsize) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) is an **INT** value that specifies the new width, in pixels. The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) is an **INT** value that specifies the new height, in pixels.

</dd> </dl>

## Return value

Returns the old width and height. The width is in the [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) of the return value, and the height is in the [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)).

## Remarks

If the width is set to a value less than the image width set by [**ImageList\_Create**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_create), the width of the tab is set to the lowest value that is greater than the image width.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

