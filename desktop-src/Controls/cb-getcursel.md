---
title: CB_GETCURSEL message (Winuser.h)
description: An application sends a CB\_GETCURSEL message to retrieve the index of the currently selected item, if any, in the list box of a combo box.
ms.assetid: 47bf87f6-637f-48e9-849e-b2acbe5a6a7b
keywords:
- CB_GETCURSEL message Windows Controls
topic_type:
- apiref
api_name:
- CB_GETCURSEL
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_GETCURSEL message

An application sends a **CB\_GETCURSEL** message to retrieve the index of the currently selected item, if any, in the list box of a combo box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

The return value is the zero-based index of the currently selected item. If no item is selected, it is CB\_ERR.

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

[**CB\_SELECTSTRING**](cb-selectstring.md)
</dt> <dt>

[**CB\_SETCURSEL**](cb-setcursel.md)
</dt> </dl>

 

 





