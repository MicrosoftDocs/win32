---
title: UDM_GETRANGE32 message (Commctrl.h)
description: Retrieves the 32-bit range of an up-down control.
ms.assetid: a94b50c9-cd2f-430d-875f-720e51f544f1
keywords:
- UDM_GETRANGE32 message Windows Controls
topic_type:
- apiref
api_name:
- UDM_GETRANGE32
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# UDM\_GETRANGE32 message

Retrieves the 32-bit range of an up-down control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Pointer to a signed integer that receives the lower limit of the up-down control range. This parameter may be **NULL**.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a signed integer that receives the upper limit of the up-down control range. This parameter may be **NULL**.

</dd> </dl>

## Return value

The return value for this message is not used.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





