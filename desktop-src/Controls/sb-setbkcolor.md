---
title: SB_SETBKCOLOR message (Commctrl.h)
description: Sets the background color in a status bar.
ms.assetid: 49bcd816-e3e2-45f4-8845-ef67789b8a01
keywords:
- SB_SETBKCOLOR message Windows Controls
topic_type:
- apiref
api_name:
- SB_SETBKCOLOR
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SB\_SETBKCOLOR message

Sets the background color in a status bar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

[**COLORREF**](/windows/desktop/gdi/colorref) value that specifies the new background color. Specify the CLR\_DEFAULT value to cause the status bar to use its default background color.

</dd> </dl>

## Return value

Returns the previous background color, or CLR\_DEFAULT if the background color is the default color.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

