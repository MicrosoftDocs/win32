---
title: SB_SETMINHEIGHT message (Commctrl.h)
description: Sets the minimum height of a status window's drawing area.
ms.assetid: 346fe654-f808-4191-9c3d-f9a4def08df1
keywords:
- SB_SETMINHEIGHT message Windows Controls
topic_type:
- apiref
api_name:
- SB_SETMINHEIGHT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SB\_SETMINHEIGHT message

Sets the minimum height of a status window's drawing area.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Minimum height, in pixels, of the window.

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

No return value.

## Remarks

The minimum height is the sum of *wParam* and twice the width, in pixels, of the vertical border of the status window. An application must send the [**WM\_SIZE**](/windows/desktop/winmsg/wm-size) message to the status window to redraw the window. The *wParam* and *lParam* parameters of the **WM\_SIZE** message should be set to zero.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

