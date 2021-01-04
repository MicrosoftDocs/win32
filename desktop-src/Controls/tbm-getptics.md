---
title: TBM_GETPTICS message (Commctrl.h)
description: Retrieves the address of an array that contains the positions of the tick marks for a trackbar.
ms.assetid: d15a4b4d-2ced-40a4-9351-ed7ecc5a5751
keywords:
- TBM_GETPTICS message Windows Controls
topic_type:
- apiref
api_name:
- TBM_GETPTICS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBM\_GETPTICS message

Retrieves the address of an array that contains the positions of the tick marks for a trackbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the address of an array of **DWORD** values. The elements of the array specify the logical positions of the trackbar's tick marks, not including the first and last tick marks created by the trackbar. The logical positions can be any of the integer values in the trackbar's range of minimum to maximum slider positions.

## Remarks

The number of elements in the array is two less than the tick count returned by the [**TBM\_GETNUMTICS**](tbm-getnumtics.md) message. Note that the values in the array may include duplicate positions and may not be in sequential order. The returned pointer is valid until you change the trackbar's tick marks.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





