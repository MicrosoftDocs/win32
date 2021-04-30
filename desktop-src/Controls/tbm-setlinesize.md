---
title: TBM_SETLINESIZE message (Commctrl.h)
description: Sets the number of logical positions the trackbar's slider moves in response to keyboard input from the arrow keys, such as the or keys. The logical positions are the integer increments in the trackbar's range of minimum to maximum slider positions.
ms.assetid: 7fe3f9b8-2ddf-4460-882f-6be439f83daa
keywords:
- TBM_SETLINESIZE message Windows Controls
topic_type:
- apiref
api_name:
- TBM_SETLINESIZE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBM\_SETLINESIZE message

Sets the number of logical positions the trackbar's slider moves in response to keyboard input from the arrow keys, such as the or keys. The logical positions are the integer increments in the trackbar's range of minimum to maximum slider positions.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

New line size.

</dd> </dl>

## Return value

Returns a 32-bit value that specifies the previous line size.

## Remarks

The default setting for the line size is 1.

The trackbar also sends a [**WM\_HSCROLL**](wm-hscroll.md) or [**WM\_VSCROLL**](wm-vscroll.md) message with the TB\_LINEUP and TB\_LINEDOWN notification codes to its parent window when the user presses the arrow keys.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TBM\_GETLINESIZE**](tbm-getlinesize.md)
</dt> </dl>

 

 





