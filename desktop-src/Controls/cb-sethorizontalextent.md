---
title: CB_SETHORIZONTALEXTENT message (Winuser.h)
description: An application sends the CB\_SETHORIZONTALEXTENT message to set the width, in pixels, by which a list box can be scrolled horizontally (the scrollable width).
ms.assetid: 85e8ff4f-ad9a-451c-b791-bd442b32d716
keywords:
- CB_SETHORIZONTALEXTENT message Windows Controls
topic_type:
- apiref
api_name:
- CB_SETHORIZONTALEXTENT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# CB\_SETHORIZONTALEXTENT message

An application sends the **CB\_SETHORIZONTALEXTENT** message to set the width, in pixels, by which a list box can be scrolled horizontally (the scrollable width). If the width of the list box is smaller than this value, the horizontal scroll bar horizontally scrolls items in the list box. If the width of the list box is equal to or greater than this value, the horizontal scroll bar is hidden or, if the combo box has the [**CBS\_DISABLENOSCROLL**](combo-box-styles.md) style, disabled.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies the scrollable width of the list box, in pixels.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**CB\_GETHORIZONTALEXTENT**](cb-gethorizontalextent.md)
</dt> </dl>

 

 





