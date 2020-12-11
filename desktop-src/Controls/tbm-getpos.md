---
title: TBM_GETPOS message (Commctrl.h)
description: Retrieves the current logical position of the slider in a trackbar. The logical positions are the integer values in the trackbar's range of minimum to maximum slider positions.
ms.assetid: 6f082ab2-2f9a-4bc0-bfca-56f7b1a2d921
keywords:
- TBM_GETPOS message Windows Controls
topic_type:
- apiref
api_name:
- TBM_GETPOS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBM\_GETPOS message

Retrieves the current logical position of the slider in a trackbar. The logical positions are the integer values in the trackbar's range of minimum to maximum slider positions.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns a 32-bit value that specifies the current logical position of the trackbar's slider.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TBM\_SETPOS**](tbm-setpos.md)
</dt> </dl>

 

 





