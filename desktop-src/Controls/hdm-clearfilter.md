---
title: HDM_CLEARFILTER message (Commctrl.h)
description: Clears the filter for a given header control. You can send this message explicitly or use the Header\_ClearFilter macro.
ms.assetid: 74c0265e-68d1-4414-8fd9-20f5f041d4b4
keywords:
- HDM_CLEARFILTER message Windows Controls
topic_type:
- apiref
api_name:
- HDM_CLEARFILTER
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# HDM\_CLEARFILTER message

Clears the filter for a given header control. You can send this message explicitly or use the [**Header\_ClearFilter**](/windows/desktop/api/Commctrl/nf-commctrl-header_clearfilter) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A column value indicating which filter to clear.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns an integer. The **LRESULT** is cast to an integer that indicates **TRUE**(1) or **FALSE**(0).

## Remarks

If the column value is specified as -1, all the filters are cleared, and the [HDN\_FILTERCHANGE](hdn-filterchange.md) notification is sent only once.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**Header\_ClearAllFilters**](/windows/desktop/api/Commctrl/nf-commctrl-header_clearallfilters)
</dt> </dl>

 

 





