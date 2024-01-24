---
title: IPM_SETADDRESS message (Commctrl.h)
description: Sets the address values for all four fields in the IP address control.
ms.assetid: 52e72437-3558-4789-844f-5ab5b0b7967c
keywords:
- IPM_SETADDRESS message Windows Controls
topic_type:
- apiref
api_name:
- IPM_SETADDRESS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# IPM\_SETADDRESS message

Sets the address values for all four fields in the IP address control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

A **DWORD** value that contains the new address. The field 3 value is contained in bits 0 through 7. The field 2 value is contained in bits 8 through 15. The field 1 value is contained in bits 16 through 23. The field 0 value is contained in bits 24 through 31. The [**MAKEIPADDRESS**](/windows/desktop/api/Commctrl/nf-commctrl-makeipaddress) macro can also be used to create the address information.

</dd> </dl>

## Return value

The return value is not used.

## Remarks

This message does not generate an [**IPN\_FIELDCHANGED**](ipn-fieldchanged.md) notification.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





