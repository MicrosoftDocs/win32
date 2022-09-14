---
title: TB_GETUNICODEFORMAT message (Commctrl.h)
description: TB_GETUNICODEFORMAT message - Retrieves the Unicode character format flag for the control.
ms.assetid: aadce646-daf1-4f1e-9171-2aeac12d3484
keywords:
- TB_GETUNICODEFORMAT message Windows Controls
topic_type:
- apiref
api_name:
- TB_GETUNICODEFORMAT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_GETUNICODEFORMAT message

Retrieves the Unicode character format flag for the control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the Unicode format flag for the control. If this value is nonzero, the control is using Unicode characters. If this value is zero, the control is using ANSI characters.

## Remarks

See the remarks for [**CCM\_GETUNICODEFORMAT**](ccm-getunicodeformat.md) for a discussion of this message.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TB\_SETUNICODEFORMAT**](tb-setunicodeformat.md)
</dt> </dl>

 

 





