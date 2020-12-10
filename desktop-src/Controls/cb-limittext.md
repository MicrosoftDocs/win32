---
title: CB_LIMITTEXT message (Winuser.h)
description: Limits the length of the text the user may type into the edit control of a combo box.
ms.assetid: 95b7d07a-594b-4096-afbb-4dab77bdc41d
keywords:
- CB_LIMITTEXT message Windows Controls
topic_type:
- apiref
api_name:
- CB_LIMITTEXT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_LIMITTEXT message

Limits the length of the text the user may type into the edit control of a combo box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The maximum number of **TCHARs** the user can enter, not including the terminating null character. If this parameter is zero, the text length is limited to 0x7FFFFFFE characters.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

The return value is always **TRUE**.

## Remarks

If the combo box does not have the [**CBS\_AUTOHSCROLL**](combo-box-styles.md) style, setting the text limit to be larger than the size of the edit control has no effect.

The **CB\_LIMITTEXT** message limits only the text the user can enter. It has no effect on any text already in the edit control when the message is sent, nor does it affect the length of the text copied to the edit control when a string in the list box is selected.

The default limit to the text a user can enter in the edit control is 30,000 **TCHARs**.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



 

 





