---
title: CB_ADDSTRING message (Winuser.h)
description: Adds a string to the list box of a combo box. If the combo box does not have the CBS\_SORT style, the string is added to the end of the list. Otherwise, the string is inserted into the list, and the list is sorted.
ms.assetid: 201bcb7b-e7d1-41e6-8eb7-a5864b659a52
keywords:
- CB_ADDSTRING message Windows Controls
topic_type:
- apiref
api_name:
- CB_ADDSTRING
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_ADDSTRING message

Adds a string to the list box of a combo box. If the combo box does not have the [**CBS\_SORT**](combo-box-styles.md) style, the string is added to the end of the list. Otherwise, the string is inserted into the list, and the list is sorted.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

An **LPCTSTR** pointer to the null-terminated string to be added. If you create the combo box with an owner-drawn style but without the [**CBS\_HASSTRINGS**](combo-box-styles.md) style, the value of the *lParam* parameter is stored as item data rather than the string it would otherwise point to. The item data can be retrieved or modified by sending the [**CB\_GETITEMDATA**](cb-getitemdata.md) or [**CB\_SETITEMDATA**](cb-setitemdata.md) message.

</dd> </dl>

## Return value

The return value is the zero-based index to the string in the list box of the combo box. If an error occurs, the return value is CB\_ERR. If insufficient space is available to store the new string, it is CB\_ERRSPACE.

## Remarks

If you create an owner-drawn combo box with the [**CBS\_SORT**](combo-box-styles.md) style but without the [**CBS\_HASSTRINGS**](combo-box-styles.md) style, the [**WM\_COMPAREITEM**](wm-compareitem.md) message is sent one or more times to the owner of the combo box so the new item can be properly placed in the list.

To insert a string at a specific location within the list, use the [**CB\_INSERTSTRING**](cb-insertstring.md) message.

If the combo box has [**WS\_HSCROLL**](/windows/desktop/winmsg/window-styles) style and you add a string wider than the combo box, send a [**LB\_SETHORIZONTALEXTENT**](lb-sethorizontalextent.md) message to ensure the horizontal scroll bar appears.

**Comclt32.dll version 5.0 or later:** If [**CBS\_LOWERCASE**](combo-box-styles.md) or [**CBS\_UPPERCASE**](combo-box-styles.md) is set, the Unicode version of **CB\_ADDSTRING** alters the string. If using read-only global memory, this causes the application to fail.

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

[**CB\_DIR**](cb-dir.md)
</dt> <dt>

[**CB\_INSERTSTRING**](cb-insertstring.md)
</dt> <dt>

[**LB\_SETHORIZONTALEXTENT**](lb-sethorizontalextent.md)
</dt> <dt>

[**WM\_COMPAREITEM**](wm-compareitem.md)
</dt> </dl>

 

