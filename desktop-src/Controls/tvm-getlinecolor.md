---
title: TVM_GETLINECOLOR message (Commctrl.h)
description: The TVM\_GETLINECOLOR message gets the current line color.
ms.assetid: e74441b3-5d4f-4454-b896-2e96ce649419
keywords:
- TVM_GETLINECOLOR message Windows Controls
topic_type:
- apiref
api_name:
- TVM_GETLINECOLOR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_GETLINECOLOR message

The **TVM\_GETLINECOLOR** message gets the current line color.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the current line color, or the CLR\_DEFAULT value if none has been specified.

## Remarks

This message only retrieves line colors. To retrieve the colors of the '+' and '-' inside the buttons, use the [**TVM\_GETTEXTCOLOR**](tvm-gettextcolor.md) message.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TVM\_SETLINECOLOR**](tvm-setlinecolor.md)
</dt> </dl>

 

 





