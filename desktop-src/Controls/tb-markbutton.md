---
title: TB_MARKBUTTON message (Commctrl.h)
description: Sets the highlight state of a given button in a toolbar control.
ms.assetid: cba0e2d2-40a7-4e20-a1ef-d5f5444c96d9
keywords:
- TB_MARKBUTTON message Windows Controls
topic_type:
- apiref
api_name:
- TB_MARKBUTTON
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_MARKBUTTON message

Sets the highlight state of a given button in a toolbar control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Command identifier for a toolbar button.

</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) is a **BOOL** that indicates the new highlight state. If **TRUE**, the button is highlighted. If **FALSE**, the button is set to its default state.

The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) must be zero.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

