---
title: TB_SETBUTTONWIDTH message (Commctrl.h)
description: Sets the minimum and maximum button widths in the toolbar control.
ms.assetid: 3311216a-e0b2-48bb-bad7-0a04185573cf
keywords:
- TB_SETBUTTONWIDTH message Windows Controls
topic_type:
- apiref
api_name:
- TB_SETBUTTONWIDTH
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_SETBUTTONWIDTH message

Sets the minimum and maximum button widths in the toolbar control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) specifies the minimum button width, in pixels. Toolbar buttons will never be narrower than this value.

The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) specifies the maximum button width, in pixels. If button text is too wide, the control displays it with ellipsis points.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Remarks

Use **TB\_SETBUTTONWIDTH** to set the maximum and minimum allowed widths for buttons before they are added. Use [**TB\_SETBUTTONSIZE**](tb-setbuttonsize.md) to set the actual size of buttons.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

