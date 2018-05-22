---
title: EM\_GETTEXTRANGE message
description: Retrieves a specified range of characters from a rich edit control.
ms.assetid: '18398963-eb2c-4f64-99f5-9614a5d34b52'
keywords: ["EM_GETTEXTRANGE message Windows Controls"]
topic_type:
- apiref
api_name:
- EM_GETTEXTRANGE
api_location:
- Richedit.h
api_type:
- HeaderDef
---

# EM\_GETTEXTRANGE message

Retrieves a specified range of characters from a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TEXTRANGE**](textrange.md) structure that specifies the range of characters to retrieve and a buffer to copy the characters to.

</dd> </dl>

## Return value

The message returns the number of characters copied, not including the terminating null character.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**TEXTRANGE**](textrange.md)
</dt> </dl>

 

 





