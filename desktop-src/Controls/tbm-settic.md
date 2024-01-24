---
title: TBM_SETTIC message (Commctrl.h)
description: Sets a tick mark in a trackbar at the specified logical position.
ms.assetid: 89b42cac-967e-40c7-9fab-2bd76f06f3f9
keywords:
- TBM_SETTIC message Windows Controls
topic_type:
- apiref
api_name:
- TBM_SETTIC
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBM\_SETTIC message

Sets a tick mark in a trackbar at the specified logical position.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Position of the tick mark. This parameter can be any of the integer values in the trackbar's range of minimum to maximum slider positions.

</dd> </dl>

## Return value

Returns **TRUE** if the tick mark is set, or **FALSE** otherwise.

## Remarks

A trackbar creates its own first and last tick marks. Do not use this message to set the first and last tick marks.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**TBM\_GETPTICS**](tbm-getptics.md)
</dt> <dt>

[**TBM\_GETTIC**](tbm-gettic.md)
</dt> </dl>

 

 





