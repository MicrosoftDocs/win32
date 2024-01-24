---
title: SB_SETUNICODEFORMAT message (Commctrl.h)
description: SB_SETUNICODEFORMAT message - Sets the Unicode character format flag for the control. This message allows you to change the character set used by the control at run time rather than having to re-create the control.
ms.assetid: 022e7138-c12f-4c59-82da-2ac6d276fa77
keywords:
- SB_SETUNICODEFORMAT message Windows Controls
topic_type:
- apiref
api_name:
- SB_SETUNICODEFORMAT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SB\_SETUNICODEFORMAT message

Sets the Unicode character format flag for the control. This message allows you to change the character set used by the control at run time rather than having to re-create the control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Determines the character set that is used by the control. If this value is **TRUE**, the control will use Unicode characters. If this value is **FALSE**, the control will use ANSI characters.

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

[**SB\_GETUNICODEFORMAT**](sb-getunicodeformat.md)
</dt> </dl>

 

 





