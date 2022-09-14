---
title: TBM_GETSELEND message (Commctrl.h)
description: Retrieves the ending position of the current selection range in a trackbar.
ms.assetid: e365dd4d-eb49-4107-b6d4-cdb558d27fdb
keywords:
- TBM_GETSELEND message Windows Controls
topic_type:
- apiref
api_name:
- TBM_GETSELEND
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBM\_GETSELEND message

Retrieves the ending position of the current selection range in a trackbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns a 32-bit value that specifies the ending position of the current selection range.

## Remarks

A trackbar can have a selection range only if you specified the [**TBS\_ENABLESELRANGE**](trackbar-control-styles.md) style when you created it.

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

[**TBM\_GETSELSTART**](tbm-getselstart.md)
</dt> <dt>

[**TBM\_SETSEL**](tbm-setsel.md)
</dt> <dt>

[**TBM\_SETSELEND**](tbm-setselend.md)
</dt> <dt>

[**TBM\_SETSELSTART**](tbm-setselstart.md)
</dt> </dl>

 

 





