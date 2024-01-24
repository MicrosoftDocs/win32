---
title: TDM_SET_MARQUEE_PROGRESS_BAR message (Commctrl.h)
description: Indicates whether the hosted progress bar of a task dialog should be displayed in marquee mode.
ms.assetid: 28b9b519-6b96-4130-936c-b8fe8df86d25
keywords:
- TDM_SET_MARQUEE_PROGRESS_BAR message Windows Controls
topic_type:
- apiref
api_name:
- TDM_SET_MARQUEE_PROGRESS_BAR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TDM\_SET\_MARQUEE\_PROGRESS\_BAR message

Indicates whether the hosted progress bar of a task dialog should be displayed in marquee mode.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

A **BOOL** that indicates whether the progress bar should be shown in marquee mode. A value of **TRUE** turns on marquee mode, and a value of **FALSE** turns off marquee mode.

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

The return value is ignored.

## Remarks

For information on marquee mode, see [Progress Bar Control](progress-bar-control.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





