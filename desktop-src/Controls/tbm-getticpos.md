---
title: TBM_GETTICPOS message (Commctrl.h)
description: Retrieves the current physical position of a tick mark in a trackbar.
ms.assetid: a4b0ec32-ef4e-4607-ade1-5e2be02bebe4
keywords:
- TBM_GETTICPOS message Windows Controls
topic_type:
- apiref
api_name:
- TBM_GETTICPOS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBM\_GETTICPOS message

Retrieves the current physical position of a tick mark in a trackbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Zero-based index identifying a tick mark. The positions of the first and last tick marks are not directly available via this message.

</dd> <dt>

*lParam* 
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

Returns the distance, in client coordinates, from the left or top of the trackbar's client area to the specified tick mark. The return value is the x-coordinate of the tick mark for a horizontal trackbar or the y-coordinate for a vertical trackbar. If *wParam* is not a valid index, the return value is -1.

## Remarks

Because the first and last tick marks are not available through this message, valid indexes are offset from their tick position on the trackbar. If the difference between [**TBM\_GETRANGEMIN**](tbm-getrangemin.md) and [**TBM\_GETRANGEMAX**](tbm-getrangemax.md) is less than two, then there is no valid index and this message will fail.

The following illustrates the relation between the ticks on a trackbar, the ticks available through this message, and their zero-based indexes.

``` syntax
0 1 2 3 4 5 6 7 8 9    // Tick positions seen on the trackbar.
  1 2 3 4 5 6 7 8      // Tick positions whose position can be identified.
  0 1 2 3 4 5 6 7      // Index numbers for the identifiable positions.
```

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





