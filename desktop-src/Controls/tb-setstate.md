---
title: TB_SETSTATE message (Commctrl.h)
description: Sets the state for the specified button in a toolbar.
ms.assetid: 68633b58-8d21-4931-b01f-32a66bda37b1
keywords:
- TB_SETSTATE message Windows Controls
topic_type:
- apiref
api_name:
- TB_SETSTATE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_SETSTATE message

Sets the state for the specified button in a toolbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Command identifier of the button.

</dd> <dt>

*lParam* 
</dt> <dd>

The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) is a combination of values listed in [Toolbar Button States](toolbar-button-states.md). The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) must be zero.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

