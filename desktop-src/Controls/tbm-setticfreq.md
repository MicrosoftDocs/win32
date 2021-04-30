---
title: TBM_SETTICFREQ message (Commctrl.h)
description: Sets the interval frequency for tick marks in a trackbar.
ms.assetid: c391260c-d6c2-4b6a-84e8-7fe5d734035b
keywords:
- TBM_SETTICFREQ message Windows Controls
topic_type:
- apiref
api_name:
- TBM_SETTICFREQ
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBM\_SETTICFREQ message

Sets the interval frequency for tick marks in a trackbar. For example, if the frequency is set to two, a tick mark is displayed for every other increment in the trackbar's range. The default setting for the frequency is one; that is, every increment in the range is associated with a tick mark.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Frequency of the tick marks.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

No return value.

## Remarks

The trackbar must have the [**TBS\_AUTOTICKS**](trackbar-control-styles.md) style to use this message.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





