---
title: EM_SETCARETINDEX message (CommCtrl.h)
description: Sets the zero-based index value of the position of the caret in an edit control.
ms.assetid: 5cb7ff1e-18e8-49c8-8072-872cf32b18b0
keywords:
- EM_SETCARETINDEX message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETCARETINDEX
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 10/19/2018
---

# EM\_SETCARETINDEX message

Sets the zero-based index value of the position of the caret in an edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The new zero-based index value of the position of the caret.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

This message does not return a value.

## Remarks

If the index is out of the range of the text in an edit control, the index will be adjusted to fit inside the range of the text.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, 1809 \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2019 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>CommCtrl.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EM\_GETCARETINDEX**](em-getcaretindex.md)
</dt> </dl>

 

 





