---
title: TBM_GETTIC message (Commctrl.h)
description: Retrieves the logical position of a tick mark in a trackbar. The logical position can be any of the integer values in the trackbar's range of minimum to maximum slider positions.
ms.assetid: 9d70c860-de97-4579-bb10-e9e9db7f1784
keywords:
- TBM_GETTIC message Windows Controls
topic_type:
- apiref
api_name:
- TBM_GETTIC
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBM\_GETTIC message

Retrieves the logical position of a tick mark in a trackbar. The logical position can be any of the integer values in the trackbar's range of minimum to maximum slider positions.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Zero-based index identifying a tick mark. Valid indexes are in the range from zero to two less than the tick count returned by the [**TBM\_GETNUMTICS**](tbm-getnumtics.md) message.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the logical position of the specified tick mark, or -1 if *wParam* does not specify a valid index.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





