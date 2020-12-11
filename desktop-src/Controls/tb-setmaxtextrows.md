---
title: TB_SETMAXTEXTROWS message (Commctrl.h)
description: Sets the maximum number of text rows displayed on a toolbar button.
ms.assetid: a14d74e8-cc21-482d-9bca-38dc7c0528ec
keywords:
- TB_SETMAXTEXTROWS message Windows Controls
topic_type:
- apiref
api_name:
- TB_SETMAXTEXTROWS
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_SETMAXTEXTROWS message

Sets the maximum number of text rows displayed on a toolbar button.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Maximum number of rows of text that can be displayed.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Remarks

To cause text to wrap, you must set the maximum button width by sending a [**TB\_SETBUTTONWIDTH**](tb-setbuttonwidth.md) message. The text wraps at a word break; line breaks ("\\n") in the text are ignored. Text in TBSTYLE\_LIST toolbars is always shown on a single line.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





