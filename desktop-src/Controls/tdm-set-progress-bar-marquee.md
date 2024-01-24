---
title: TDM_SET_PROGRESS_BAR_MARQUEE message (Commctrl.h)
description: Starts and stops the marquee display of the progress bar in a task dialog, and sets the speed of the marquee.
ms.assetid: df947171-a916-4db9-abe0-57a3bf11037f
keywords:
- TDM_SET_PROGRESS_BAR_MARQUEE message Windows Controls
topic_type:
- apiref
api_name:
- TDM_SET_PROGRESS_BAR_MARQUEE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TDM\_SET\_PROGRESS\_BAR\_MARQUEE message

Starts and stops the marquee display of the progress bar in a task dialog, and sets the speed of the marquee.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

A **BOOL** that indicates whether to turn the marquee display on or off. Use **TRUE** to turn on the marquee display, or **FALSE** to turn it off.

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

A **UINT** that specifies the time, in milliseconds, between marquee animation updates. If this parameter is zero, the marquee animation is updated every 30 milliseconds.

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



 

 





