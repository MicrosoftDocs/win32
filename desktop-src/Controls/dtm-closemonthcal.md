---
title: DTM_CLOSEMONTHCAL message (Commctrl.h)
description: Closes a date and time picker (DTP) control. Send this message explicitly or by using the DateTime\_CloseMonthCal macro.
ms.assetid: f60af77f-ec34-4f3d-9427-cda7ac6083bf
keywords:
- DTM_CLOSEMONTHCAL message Windows Controls
topic_type:
- apiref
api_name:
- DTM_CLOSEMONTHCAL
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DTM\_CLOSEMONTHCAL message

Closes a date and time picker (DTP) control. Send this message explicitly or by using the [**DateTime\_CloseMonthCal**](/windows/desktop/api/Commctrl/nf-commctrl-datetime_closemonthcal) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns zero.

## Remarks

Destroys the control and sends a [DTN\_CLOSEUP](dtn-closeup.md) notification that the control is closing as opposed to the control is opening (dropping-down as in the [DTN\_DROPDOWN](dtn-dropdown.md) notification) to the control's parent.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[DTN\_DROPDOWN](dtn-dropdown.md)
</dt> <dt>

[DTN\_CLOSEUP](dtn-closeup.md)
</dt> </dl>

 

 





