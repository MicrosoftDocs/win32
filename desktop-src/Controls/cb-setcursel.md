---
title: CB_SETCURSEL message (Winuser.h)
description: An application sends a CB\_SETCURSEL message to select a string in the list of a combo box.
ms.assetid: d4ce3811-6e0a-4952-97cf-ba6efde0de0d
keywords:
- CB_SETCURSEL message Windows Controls
topic_type:
- apiref
api_name:
- CB_SETCURSEL
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_SETCURSEL message

An application sends a **CB\_SETCURSEL** message to select a string in the list of a combo box. If necessary, the list scrolls the string into view. The text in the edit control of the combo box changes to reflect the new selection, and any previous selection in the list is removed.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the zero-based index of the string to select. If this parameter is -1, any current selection in the list is removed and the edit control is cleared.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

If the message is successful, the return value is the index of the item selected. If *wParam* is greater than the number of items in the list or if *wParam* is -1, the return value is CB\_ERR and the selection is cleared.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**CB\_FINDSTRING**](cb-findstring.md)
</dt> <dt>

[**CB\_GETCURSEL**](cb-getcursel.md)
</dt> <dt>

[**CB\_SELECTSTRING**](cb-selectstring.md)
</dt> </dl>

 

 





