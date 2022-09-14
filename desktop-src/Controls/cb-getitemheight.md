---
title: CB_GETITEMHEIGHT message (Winuser.h)
description: Determines the height of list items or the selection field in a combo box.
ms.assetid: 72fba6ca-0a51-4801-bd45-5f5a7d5ebee2
keywords:
- CB_GETITEMHEIGHT message Windows Controls
topic_type:
- apiref
api_name:
- CB_GETITEMHEIGHT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_GETITEMHEIGHT message

Determines the height of list items or the selection field in a combo box.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The combo box component whose height is to be retrieved. This parameter must be -1 to retrieve the height of the selection field. It must be zero to retrieve the height of list items, unless the combo box has the [**CBS\_OWNERDRAWVARIABLE**](combo-box-styles.md) style. In that case, the *wParam* parameter is the zero-based index of a specific list item.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

The return value is the height, in pixels, of the list items in a combo box. If the combo box has the [**CBS\_OWNERDRAWVARIABLE**](combo-box-styles.md) style, it is the height of the item specified by the *wParam* parameter. If *wParam* is -1, the return value is the height of the edit control (or static-text) portion of the combo box. If an error occurs, the return value is CB\_ERR.

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

[**CB\_SETITEMHEIGHT**](cb-setitemheight.md)
</dt> <dt>

[**WM\_MEASUREITEM**](wm-measureitem.md)
</dt> </dl>

 

 





