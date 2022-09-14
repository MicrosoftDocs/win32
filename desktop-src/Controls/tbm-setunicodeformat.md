---
title: TBM_SETUNICODEFORMAT message (Commctrl.h)
description: TBM_SETUNICODEFORMAT message - Sets the Unicode character format flag for the control. This message allows you to change the character set used by the control at run time rather than having to re-create the control.
ms.assetid: c50a49e8-6042-490d-bb7b-baf917d5c30a
keywords:
- TBM_SETUNICODEFORMAT message Windows Controls
topic_type:
- apiref
api_name:
- TBM_SETUNICODEFORMAT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TBM\_SETUNICODEFORMAT message

Sets the Unicode character format flag for the control. This message allows you to change the character set used by the control at run time rather than having to re-create the control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Determines the character set that is used by the control. If this value is nonzero, the control will use Unicode characters. If this value is zero, the control will use ANSI characters.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the previous Unicode format flag for the control.

## Remarks

See the remarks for [**CCM\_SETUNICODEFORMAT**](ccm-setunicodeformat.md) for a discussion of this message.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TBM\_GETUNICODEFORMAT**](tbm-getunicodeformat.md)
</dt> </dl>

 

 





