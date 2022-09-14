---
title: RB_SETPALETTE message (Commctrl.h)
description: Sets the rebar control's current palette.
ms.assetid: 85f0726a-21fd-41b3-aa52-6a0a0c1947fa
keywords:
- RB_SETPALETTE message Windows Controls
topic_type:
- apiref
api_name:
- RB_SETPALETTE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# RB\_SETPALETTE message

Sets the rebar control's current palette.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

An **HPALETTE** that specifies the new palette that the rebar control will use.

</dd> </dl>

## Return value

Returns an **HPALETTE** that specifies the rebar control's previous palette.

## Remarks

It is the responsibility of the application sending this message to delete the **HPALETTE** passed in this message (see [**DeleteObject**](/windows/desktop/api/wingdi/nf-wingdi-deleteobject)). The rebar control will not delete an **HPALETTE** set with this message.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**RB\_GETPALETTE**](rb-getpalette.md)
</dt> </dl>

 

