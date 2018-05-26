---
title: CB\_GETHORIZONTALEXTENT message
description: Gets the width, in pixels, that the list box can be scrolled horizontally (the scrollable width). This is applicable only if the list box has a horizontal scroll bar.
ms.assetid: 7c9fff88-2750-4c94-b7f6-6bdd81c224e9
keywords:
- CB_GETHORIZONTALEXTENT message Windows Controls
topic_type:
- apiref
api_name:
- CB_GETHORIZONTALEXTENT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CB\_GETHORIZONTALEXTENT message

Gets the width, in pixels, that the list box can be scrolled horizontally (the scrollable width). This is applicable only if the list box has a horizontal scroll bar.

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

The return value is the scrollable width, in pixels.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[**CB\_SETHORIZONTALEXTENT**](cb-sethorizontalextent.md)
</dt> </dl>

 

 





