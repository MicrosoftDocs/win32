---
title: TBM_GETNUMTICS message (Commctrl.h)
description: Retrieves the number of tick marks in a trackbar.
ms.assetid: 3c3f7ebb-a544-474c-ba14-68eae543ee38
keywords:
- TBM_GETNUMTICS message Windows Controls
topic_type:
- apiref
api_name:
- TBM_GETNUMTICS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBM\_GETNUMTICS message

Retrieves the number of tick marks in a trackbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

If no [tick flag](trackbar-control-styles.md) is set, it returns 2 for the beginning and ending ticks. If [**TBS\_NOTICKS**](trackbar-control-styles.md) is set, it returns zero. Otherwise, it takes the difference between the range minimum and maximum, divides by the tick frequency, and adds 2.

## Remarks

The **TBM\_GETNUMTICS** message counts all of the tick marks, including the first and last tick marks created by the trackbar.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





