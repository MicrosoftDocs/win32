---
title: TVM_SETLINECOLOR message (Commctrl.h)
description: The TVM\_SETLINECOLOR message sets the current line color.
ms.assetid: c5fc28af-5603-489f-aa6b-73e153f9aebc
keywords:
- TVM_SETLINECOLOR message Windows Controls
topic_type:
- apiref
api_name:
- TVM_SETLINECOLOR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVM\_SETLINECOLOR message

The **TVM\_SETLINECOLOR** message sets the current line color.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

New line color. Use the CLR\_DEFAULT value to restore the system default colors.

</dd> </dl>

## Return value

Returns the previous line color.

## Remarks

This message only changes line colors. To change the colors of the '+' and '-' inside the buttons, use the [**TVM\_SETTEXTCOLOR**](tvm-settextcolor.md) message.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TVM\_GETLINECOLOR**](tvm-getlinecolor.md)
</dt> </dl>

 

 





