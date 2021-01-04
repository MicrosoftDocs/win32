---
title: TB_CHECKBUTTON message (Commctrl.h)
description: Checks or unchecks a given button in a toolbar.
ms.assetid: e67734a9-851c-41ab-8ad7-15d434f58e5a
keywords:
- TB_CHECKBUTTON message Windows Controls
topic_type:
- apiref
api_name:
- TB_CHECKBUTTON
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_CHECKBUTTON message

Checks or unchecks a given button in a toolbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Command identifier of the button to check.

</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) is a **BOOL** that indicates whether to check or uncheck the specified button. If **TRUE**, the check is added. If **FALSE**, the check is removed.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

When a button is checked, it is displayed in the pressed state.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

