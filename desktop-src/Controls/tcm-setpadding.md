---
title: TCM_SETPADDING message (Commctrl.h)
description: Sets the amount of space (padding) around each tab's icon and label in a tab control. You can send this message explicitly or by using the TabCtrl\_SetPadding macro.
ms.assetid: c7f84c0d-8bf4-429a-b403-a0019575e72e
keywords:
- TCM_SETPADDING message Windows Controls
topic_type:
- apiref
api_name:
- TCM_SETPADDING
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TCM\_SETPADDING message

Sets the amount of space (padding) around each tab's icon and label in a tab control. You can send this message explicitly or by using the [**TabCtrl\_SetPadding**](/windows/desktop/api/Commctrl/nf-commctrl-tabctrl_setpadding) macro.

## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) is an **INT** value that specifies the amount of horizontal padding, in pixels. The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) is an **INT** value that specifies the amount of vertical padding, in pixels.

</dd> </dl>

## Return value

No return value.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

