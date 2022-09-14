---
title: DTM_SETMCFONT message (Commctrl.h)
description: Sets the font to be used by the date and time picker (DTP) control's child month calendar control. You can send this message explicitly or use the DateTime\_SetMonthCalFont macro.
ms.assetid: 5033e975-9b68-438a-99c3-80ca02cd59e7
keywords:
- DTM_SETMCFONT message Windows Controls
topic_type:
- apiref
api_name:
- DTM_SETMCFONT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DTM\_SETMCFONT message

Sets the font to be used by the date and time picker (DTP) control's child month calendar control. You can send this message explicitly or use the [**DateTime\_SetMonthCalFont**](/windows/desktop/api/Commctrl/nf-commctrl-datetime_setmonthcalfont) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the font that will be set.

</dd> <dt>

*lParam* 
</dt> <dd>

Specifies whether the control should be redrawn immediately upon setting the font. Setting this parameter to **TRUE** causes the control to redraw itself.

</dd> </dl>

## Return value

The return value for this message is not used.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





