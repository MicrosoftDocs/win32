---
title: EM_SETSCROLLPOS message (Richedit.h)
description: Scrolls the contents of a rich edit control to the specified point.
ms.assetid: 9ec514a4-97b1-44ab-b2ca-973b1f6fc404
keywords:
- EM_SETSCROLLPOS message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETSCROLLPOS
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETSCROLLPOS message

Scrolls the contents of a rich edit control to the specified point.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used; it must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**POINT**](/previous-versions//dd162805(v=vs.85)) structure which specifies a point in the virtual text space of the document, expressed in pixels. The document will be scrolled until this point is located in the upper-left corner of the edit control window. If you want to change the view such that the upper left corner of the view is two lines down and one character in from the left edge. You would pass a point of (7, 22).

The rich edit control checks the x and y coordinates and adjusts them if necessary, so that a complete line is displayed at the top. It also ensures that the text is never completely scrolled off the view rectangle.

</dd> </dl>

## Return value

This message always returns 1.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Redistributable<br/>          | Rich Edit 3.0<br/>                                                              |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_GETSCROLLPOS**](em-getscrollpos.md)
</dt> </dl>

 

