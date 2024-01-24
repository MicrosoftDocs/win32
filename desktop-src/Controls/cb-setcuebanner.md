---
title: CB_SETCUEBANNER message (Winuser.h)
description: Sets the cue banner text that is displayed for the edit control of a combo box.
ms.assetid: 4b2b5042-ba64-4e3f-adeb-9aea66773b0e
keywords:
- CB_SETCUEBANNER message Windows Controls
topic_type:
- apiref
api_name:
- CB_SETCUEBANNER
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_SETCUEBANNER message

Sets the cue banner text that is displayed for the edit control of a combo box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a null-terminated Unicode string buffer that contains the text.

</dd> </dl>

## Return value

Returns 1 if successful, or an error value otherwise.

## Remarks

The cue banner is text that is displayed in the edit control of a combo box when there is no selection.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>CommCtrl.h</dt> </dl> |



## See also

<dl> <dt>

[Combo Box Features](combo-box-features.md)
</dt> </dl>

 

 





