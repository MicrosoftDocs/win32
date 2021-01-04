---
title: LB_GETHORIZONTALEXTENT message (Winuser.h)
description: Gets the width, in pixels, that a list box can be scrolled horizontally (the scrollable width) if the list box has a horizontal scroll bar.
ms.assetid: 52461724-c06a-436a-ac95-94c5189ba37e
keywords:
- LB_GETHORIZONTALEXTENT message Windows Controls
topic_type:
- apiref
api_name:
- LB_GETHORIZONTALEXTENT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LB\_GETHORIZONTALEXTENT message

Gets the width, in pixels, that a list box can be scrolled horizontally (the scrollable width) if the list box has a horizontal scroll bar.

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

The return value is the scrollable width, in pixels, of the list box.

## Remarks

To respond to the **LB\_GETHORIZONTALEXTENT** message, the list box must have been defined with the [**WS\_HSCROLL**](/windows/desktop/winmsg/window-styles) style.

If the application does not set the horizontal extent of the list box (using [**LB\_SETHORIZONTALEXTENT**](lb-sethorizontalextent.md)), the default horizontal extent is zero. Note that the list box does not update its horizontal extent dynamically.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**LB\_SETHORIZONTALEXTENT**](lb-sethorizontalextent.md)
</dt> </dl>

 

