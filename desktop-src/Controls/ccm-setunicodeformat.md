---
title: CCM_SETUNICODEFORMAT message (Commctrl.h)
description: Sets the Unicode character format flag for the control. This message enables you to change the character set used by the control at run time rather than having to re-create the control.
ms.assetid: 8028b7d7-30d2-4154-81c7-ba1ed095ef02
keywords:
- CCM_SETUNICODEFORMAT message Windows Controls
topic_type:
- apiref
api_name:
- CCM_SETUNICODEFORMAT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CCM\_SETUNICODEFORMAT message

Sets the Unicode character format flag for the control. This message enables you to change the character set used by the control at run time rather than having to re-create the control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A value that determines the character set that is used by the control. If this value is **TRUE**, the control will use Unicode characters. If this value is **FALSE**, the control will use ANSI characters.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns the previous Unicode format flag for the control.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**CCM\_GETUNICODEFORMAT**](ccm-getunicodeformat.md)
</dt> </dl>

 

 





