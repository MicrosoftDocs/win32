---
title: RB\_SETBARINFO message
description: Sets the characteristics of a rebar control.
ms.assetid: 'e4413d46-574f-4ccd-b5fd-3ba6c1e3924b'
keywords: ["RB_SETBARINFO message Windows Controls"]
topic_type:
- apiref
api_name:
- RB_SETBARINFO
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# RB\_SETBARINFO message

Sets the characteristics of a rebar control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**REBARINFO**](rebarinfo.md) structure that contains the information to be set. You must set the **cbSize** member of this structure to **sizeof**(REBARINFO) before sending this message.

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





