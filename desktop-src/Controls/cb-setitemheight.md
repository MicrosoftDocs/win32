---
title: CB_SETITEMHEIGHT message (Winuser.h)
description: An application sends a CB\_SETITEMHEIGHT message to set the height of list items or the selection field in a combo box.
ms.assetid: 25a01170-5ffc-4d86-b696-706f5375570b
keywords:
- CB_SETITEMHEIGHT message Windows Controls
topic_type:
- apiref
api_name:
- CB_SETITEMHEIGHT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_SETITEMHEIGHT message

An application sends a **CB\_SETITEMHEIGHT** message to set the height of list items or the selection field in a combo box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the component of the combo box for which to set the height.

This parameter must be  1 to set the height of the selection field. It must be zero to set the height of list items, unless the combo box has the [**CBS\_OWNERDRAWVARIABLE**](combo-box-styles.md) style. In that case, the *wParam* parameter is the zero-based index of a specific list item.

</dd> <dt>

*lParam* 
</dt> <dd>

Specifies the height, in pixels, of the combo box component identified by *wParam*.

</dd> </dl>

## Return value

If the index or height is invalid, the return value is CB\_ERR.

## Remarks

The selection field height in a combo box is set independently of the height of the list items. An application must ensure that the height of the selection field is not smaller than the height of a particular list item.

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

[**CB\_GETITEMHEIGHT**](cb-getitemheight.md)
</dt> <dt>

[**WM\_MEASUREITEM**](wm-measureitem.md)
</dt> </dl>

 

 





