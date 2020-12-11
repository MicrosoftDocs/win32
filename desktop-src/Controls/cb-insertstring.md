---
title: CB_INSERTSTRING message (Winuser.h)
description: Inserts a string or item data into the list of a combo box. Unlike the CB\_ADDSTRING message, the CB\_INSERTSTRING message does not cause a list with the CBS\_SORT style to be sorted.
ms.assetid: b9067b4e-afca-4c78-9ca2-c717b99c7459
keywords:
- CB_INSERTSTRING message Windows Controls
topic_type:
- apiref
api_name:
- CB_INSERTSTRING
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_INSERTSTRING message

Inserts a string or item data into the list of a combo box. Unlike the [**CB\_ADDSTRING**](cb-addstring.md) message, the **CB\_INSERTSTRING** message does not cause a list with the [**CBS\_SORT**](combo-box-styles.md) style to be sorted.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The zero-based index of the position at which to insert the string. If this parameter is -1, the string is added to the end of the list.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to the null-terminated string to be inserted. If you create the combo box with an owner-drawn style but without the [**CBS\_HASSTRINGS**](combo-box-styles.md) style, the value of the *lParam* parameter is stored rather than the string to which it would otherwise point.

</dd> </dl>

## Return value

The return value is the index of the position at which the string was inserted. If an error occurs, the return value is CB\_ERR. If there is insufficient space available to store the new string, it is CB\_ERRSPACE.

If the combo box has [**WS\_HSCROLL**](/windows/desktop/winmsg/window-styles) style and you insert a string wider than the combo box, you should send a [**LB\_SETHORIZONTALEXTENT**](lb-sethorizontalextent.md) message to ensure the horizontal scroll bar appears.

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

[**CB\_ADDSTRING**](cb-addstring.md)
</dt> <dt>

[**LB\_SETHORIZONTALEXTENT**](lb-sethorizontalextent.md)
</dt> <dt>

[**CB\_DIR**](cb-dir.md)
</dt> </dl>

 

