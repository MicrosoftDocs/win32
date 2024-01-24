---
title: TBM_CLEARSEL message (Commctrl.h)
description: Clears the current selection range in a trackbar.
ms.assetid: ccf69fb7-d616-4a7a-8c7c-7a82827758b1
keywords:
- TBM_CLEARSEL message Windows Controls
topic_type:
- apiref
api_name:
- TBM_CLEARSEL
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBM\_CLEARSEL message

Clears the current selection range in a trackbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Redraw flag. If this parameter is **TRUE**, the trackbar is redrawn after the selection is cleared.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

No return value.

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

[**TBM\_SETSEL**](tbm-setsel.md)
</dt> <dt>

[**TBM\_SETSELEND**](tbm-setselend.md)
</dt> <dt>

[**TBM\_SETSELSTART**](tbm-setselstart.md)
</dt> </dl>

 

 





