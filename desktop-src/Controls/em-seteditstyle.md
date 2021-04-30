---
title: EM_SETEDITSTYLE message (Richedit.h)
description: Sets the current edit style flags for a rich edit control.
ms.assetid: e48de6b3-0fd2-4791-9863-a6dcdafa3642
keywords:
- EM_SETEDITSTYLE message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETEDITSTYLE
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETEDITSTYLE message

Sets the current edit style flags for a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies one or more edit style flags. For a list of possible values, see [**EM\_GETEDITSTYLE**](em-geteditstyle.md).

</dd> <dt>

*lParam* 
</dt> <dd>

A mask consisting of one or more of the *wParam* values. Only the values specified in this mask will be set or cleared. This allows a single flag to be set or cleared without reading the current flag states.

</dd> </dl>

## Return value

The return value is the state of the edit style flags after the rich edit control has attempted to implement your edit style changes. The edit style flags are a set of flags that indicate the current edit style.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Redistributable<br/>          | Rich Edit 3.0<br/>                                                              |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_GETEDITSTYLE**](em-geteditstyle.md)
</dt> </dl>

 

 





