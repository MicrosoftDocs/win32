---
title: TTM_WINDOWFROMPOINT message (Commctrl.h)
description: Allows a subclass procedure to cause a tooltip to display text for a window other than the one beneath the mouse cursor.
ms.assetid: f3bf6917-1745-4e4f-a9c1-8fe86b2b3906
keywords:
- TTM_WINDOWFROMPOINT message Windows Controls
topic_type:
- apiref
api_name:
- TTM_WINDOWFROMPOINT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TTM\_WINDOWFROMPOINT message

Allows a subclass procedure to cause a tooltip to display text for a window other than the one beneath the mouse cursor.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**POINT**](/windows/win32/api/windef/ns-windef-point) structure that defines the point to be checked.

</dd> </dl>

## Return value

The return value is the handle to the window that contains the point, or **NULL** if no window exists at the specified point.

## Remarks

This message is intended to be processed by an application that subclasses a tooltip. It is not intended to be sent by an application. A tooltip sends this message to itself before displaying the text for a window. By changing the coordinates of the point specified by *lParam*, the subclass procedure can cause the tooltip to display text for a window other than the one beneath the mouse cursor.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

