---
title: TTM_SETMAXTIPWIDTH message (Commctrl.h)
description: Sets the maximum width for a tooltip window.
ms.assetid: 3cfb6011-d0c3-4a57-aead-d4ec09a057cc
keywords:
- TTM_SETMAXTIPWIDTH message Windows Controls
topic_type:
- apiref
api_name:
- TTM_SETMAXTIPWIDTH
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TTM\_SETMAXTIPWIDTH message

Sets the maximum width for a tooltip window.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Maximum tooltip window width, or -1 to allow any width.

</dd> </dl>

## Return value

Returns the previous maximum tooltip width.

## Remarks

The maximum width value does not indicate a tooltip window's actual width. Rather, if a tooltip string exceeds the maximum width, the control breaks the text into multiple lines, using spaces to determine line breaks. If the text cannot be segmented into multiple lines, it is displayed on a single line, which may exceed the maximum tooltip width.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**TTM\_GETMAXTIPWIDTH**](ttm-getmaxtipwidth.md)
</dt> </dl>

 

 





